import threading
import time
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import dspy
import sys
from src.tools.parser_yaml import parse_yaml
from src.tools.read_file import read_stage2_output
from src.tools.config_process import (Stage3_Config, stage3_transform_server_config,
                                     stage3_io_related_config, stage3_control_config,
                                     stage3_dsl2nl_server_config, stage3_verify_server_config)
from src.dspy.stage3_dsl2nl import dsl2nl
from src.dspy.stage3_verify import verify
from src.dspy.stage3_transform import transform
from src.tools.save_file import save_file
from src.tools.logger import Logger
from src.parse.parse import CFG_ParserTool, build_grammars
import os # Add os import for parser_dir

logger = Logger("stage3")

class RateLimiter:
    def __init__(self, rpm=30):
        self.rpm = rpm
        self.min_interval = 60.0 / self.rpm
        self.last_called = time.time()
        self.lock = threading.Lock()

    def wait(self):
        with self.lock:
            elapsed = time.time() - self.last_called
            wait_time = max(self.min_interval - elapsed, 0)
            if wait_time > 0:
                time.sleep(wait_time)
            self.last_called = time.time()

RPM_LIMITER = RateLimiter(rpm=10)  

def process(config_sentence_pair):
    stage3_config, complete_sentence = config_sentence_pair
    
    global dsl_parser
    if dsl_parser is not None:
        try:
            if not dsl_parser.parse(complete_sentence):
                logger.warning(f"DSL sentence failed parsing and will be skipped: {complete_sentence}")
                return # Skip this sentence
            else:
                logger.info(f"DSL sentence parsed successfully: {complete_sentence}")
        except Exception as e:
            logger.error(f"Exception during DSL parsing for sentence '{complete_sentence}': {e}")
            return # Skip this sentence on parsing exception
    else:
        logger.error("DSL parser not initialized. Skipping parsing validation.") # Should not happen if build_grammars was successful

    try:
        for _ in range(stage3_config.dsl2nl_epochs):
            RPM_LIMITER.wait()
            nl_sentence = dsl2nl(
                stage3_config.d2n_model_name,
                stage3_config.d2n_prompt_path,
                stage3_config.d2n_api_key,
                stage3_config.d2n_url,
                stage3_config.d2n_cot_sample_path,
                stage3_config.d2n_train_prompt,
                stage3_config.d2n_train_dataset_path,
                stage3_config.d2n_train_metric,
                stage3_config.d2n_train_metric_threshold,
                stage3_config.grammar_path,
                stage3_config.grammar_help_path,
                complete_sentence,
                stage3_config.roles_path,
            )

            RPM_LIMITER.wait()
            verify_result = verify(
                stage3_config.v_model_name,
                stage3_config.v_api_key,
                stage3_config.v_url,
                stage3_config.v_prompt_path,
                stage3_config.grammar_path,
                stage3_config.grammar_help_path,
                complete_sentence,
                nl_sentence
            )

            if verify_result:
                dsl_nl_pair = {"nl": nl_sentence, "dsl": complete_sentence}
                save_file(stage3_config.stage3_output_path, dsl_nl_pair, "a")
                return
            else:
                for _ in range(stage3_config.transform_epochs):
                    RPM_LIMITER.wait()
                    transform_nl = transform(
                        stage3_config.t_model_name,
                        stage3_config.t_api_key,
                        stage3_config.t_url,
                        stage3_config.grammar_path,
                        stage3_config.grammar_help_path,
                        complete_sentence,
                        nl_sentence
                    )

                    RPM_LIMITER.wait()
                    verify_result = verify(
                        stage3_config.v_model_name,
                        stage3_config.v_api_key,
                        stage3_config.v_url,
                        stage3_config.v_prompt_path,
                        stage3_config.grammar_path,
                        stage3_config.grammar_help_path,
                        complete_sentence,
                        transform_nl
                    )

                    if verify_result:
                        dsl_nl_pair = {"dsl": complete_sentence, "nl": transform_nl}
                        save_file(stage3_config.stage3_output_path, dsl_nl_pair, "a")
                        return
    except Exception as e:
        logger.error(f"Error processing sentence: {str(e)}")

def architecture(stage3_config):
    complete_sentence_list = read_stage2_output(stage3_config.stage2_output_path)
    model_name = f"openai/{stage3_config.d2n_model_name}"
    
    llm = dspy.LM(
        model_name,
        api_key=stage3_config.d2n_api_key,
        api_base=stage3_config.d2n_url
    )
    dspy.configure(lm=llm)

    # 动态调整最大线程数
    max_workers = min(stage3_config.num_jobs, RPM_LIMITER.rpm // 2)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        tasks = [(stage3_config, sentence) for sentence in complete_sentence_list]
        list(tqdm(executor.map(process, tasks), total=len(complete_sentence_list)))

def stage3(config_path):
    config = parse_yaml(config_path)
    
    # 配置解析部分保持不变
    (d2n_model_name, d2n_prompt_path, d2n_api_key, d2n_url, d2n_cot_sample_path,
     d2n_train_prompt, d2n_train_dataset_path, d2n_train_metric,
     d2n_train_metric_threshold) = stage3_dsl2nl_server_config(config)
    
    (v_model_name, v_prompt_path, v_api_key, v_url) = stage3_verify_server_config(config)
    
    (t_model_name, t_prompt_path, t_api_key, t_url) = stage3_transform_server_config(config)
    
    (grammar_path, grammar_help_path, stage2_output_path,
     stage3_output_path, roles_path) = stage3_io_related_config(config)
    
    (dsl2nl_epochs, transform_epochs, num_jobs) = stage3_control_config(config)

    # 更新限速器配置
    global RPM_LIMITER
    if hasattr(config, 'api_rpm'):
        RPM_LIMITER = RateLimiter(rpm=config.api_rpm)
    
    stage3_config = Stage3_Config(
        d2n_model_name, d2n_prompt_path, d2n_api_key, d2n_url,
        d2n_cot_sample_path, d2n_train_prompt, d2n_train_dataset_path,
        d2n_train_metric, d2n_train_metric_threshold,
        v_model_name, v_prompt_path, v_api_key, v_url,
        t_model_name, t_prompt_path, t_api_key, t_url,
        grammar_path, grammar_help_path, stage2_output_path,
        stage3_output_path, roles_path, dsl2nl_epochs,
        transform_epochs, num_jobs
    )
    
    # Build grammars for parsing
    parser_dir = os.path.join(os.path.dirname(grammar_path), "generated_parser") # Define a directory for generated files
    try:
        logger.info(f"Building grammars from {grammar_path} into {parser_dir}...")
        build_grammars(grammar_path, parser_dir)
        logger.info("Grammars built successfully.")
        # Instantiate the parser after building, to be passed to architecture or used in process
        global dsl_parser # Make it global or pass it around
        dsl_parser = CFG_ParserTool(grammar_path, parser_dir)
        logger.info("DSL Parser initialized.")
    except Exception as e:
        logger.error(f"Failed to build grammars or initialize parser: {e}")
        # Potentially exit if parser is critical
        # For now, we'll let it continue and it will fail in the process function if parser not init
        global dsl_parser
        dsl_parser = None # Ensure it's defined
    
    architecture(stage3_config)

if __name__ == "__main__":
    config = sys.argv[1]
    stage3(config)