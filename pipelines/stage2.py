from src.tools.parser_yaml import parse_yaml
from src.tools.read_file import read_stage1_output
from src.tools.config_process import Stage2_Config, stage2_process_verify_config, stage2_process_common_config, stage2_process_regex_config, stage2_process_control_config, stage2_process_fill_regex_config, stage2_process_transform_config
from src.dspy.stage2_verity import verify
from src.dspy.stage2_fill_regex import fill_regex
from src.dspy.stage2_transform import transform
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import sys
import dspy
from src.tools.save_file import save_file
from src.tools.logger import Logger

logger = Logger("stage2")

def process(stage2_config, skeleton_sentence):
    verify_flag = verify(
        stage2_config.v_model_name, 
        stage2_config.v_api_key, 
        stage2_config.v_url,
        stage2_config.grammar,           
        stage2_config.grammar_help, 
        skeleton_sentence,
        stage2_config.v_prompt,         
        stage2_config.re_lexical_rules_special_token
    )
    if not verify_flag:
        for idx,_ in enumerate(range(stage2_config.transform_epochs)):
            if idx == 0:
                error_msg = None
            transform_sentence = transform(
                stage2_config.transform_model_name, stage2_config.transform_api_key,
                stage2_config.transform_url, stage2_config.grammar,
                stage2_config.transform_prompt, stage2_config.grammar_help,
                skeleton_sentence,  
                stage2_config.re_lexical_rules_special_token,
                error_msg=error_msg,
            )
            verify_flag = verify(
                stage2_config.v_model_name, 
                stage2_config.v_api_key, 
                stage2_config.v_url,
                stage2_config.grammar,           
                stage2_config.grammar_help, 
                skeleton_sentence,
                stage2_config.v_prompt,         
                stage2_config.re_lexical_rules_special_token
            )
            if verify_flag:
                skeleton_sentence = transform_sentence
                break
            else:
                error_msg = transform_sentence
    if verify_flag:     
        complete_sentence, result_flag = fill_regex(
            stage2_config.fill_regex_model_name, stage2_config.fill_regex_api_key,
            stage2_config.fill_regex_url, stage2_config.fill_regex_prompt,
            stage2_config.grammar, stage2_config.grammar_help, skeleton_sentence,
            stage2_config.fill_regex_max_retries, stage2_config.re_lexical_rules_special_token,
            stage2_config.fill_regex_cot_sample_path, 
            stage2_config.fill_regex_train_prompt, 
            stage2_config.fill_regex_train_dataset_path,
            stage2_config.fill_regex_train_metric,
            stage2_config.fill_regex_train_metric_threshold,
            stage2_config.parser_dir
        )
        if result_flag:
            save_file(stage2_config.stage2_output_path, complete_sentence, 'a')

def process_wrapper(args):
    config, sentence = args
    return process(config, sentence)

def architecture(stage2_config):
    logger.info(f"begin to read stage1 output")
    skeleton_sentence_list = read_stage1_output(stage2_config.stage1_output_path)
    logger.info(f"read stage1 output done, total: {len(skeleton_sentence_list)} sentences")
    logger.info(f"begin to process with {stage2_config.num_jobs} jobs")
    model_name = "openai/" + stage2_config.v_model_name
    llm = dspy.LM(model_name, api_key=stage2_config.v_api_key, api_base=stage2_config.v_url)
    dspy.configure(lm=llm)
    with ThreadPoolExecutor(max_workers=stage2_config.num_jobs) as executor:
        args = [(stage2_config, sentence) for sentence in skeleton_sentence_list]
        list(tqdm(executor.map(lambda x: process_wrapper(x), args), total=len(skeleton_sentence_list)))

    
def stage2(config_path):
    config = parse_yaml(config_path)
    logger.info(f"stage2 config: {config}")

    (grammar, 
     grammar_help, 
     stage1_output_path, 
     stage2_output_path) = stage2_process_common_config(config)
    
    re_lexical_rules_special_token = stage2_process_regex_config(config)
    
    (transform_epochs, 
     fill_regex_max_retries,
     num_jobs) = stage2_process_control_config(config)
    
    (v_model_name, 
     v_api_key, 
     v_url, 
     v_prompt) = stage2_process_verify_config(config)
    
    (fill_regex_model_name,
     fill_regex_api_key, 
     fill_regex_url,
     fill_regex_prompt,
     fill_regex_cot_sample_path,
     fill_regex_train_prompt,
     fill_regex_train_dataset_path,
     fill_regex_train_metric,
     fill_regex_train_metric_threshold,
     parser_dir) = stage2_process_fill_regex_config(config)
    
    (transform_model_name,
     transform_api_key,
     transform_url,
     transform_prompt) = stage2_process_transform_config(config)
    
    stage2_config = Stage2_Config(
        grammar,
        grammar_help,
        stage1_output_path,
        stage2_output_path,
        re_lexical_rules_special_token,
        transform_epochs,
        fill_regex_max_retries,
        v_model_name,
        v_api_key,
        v_url,
        v_prompt,
        fill_regex_model_name,
        fill_regex_api_key,
        fill_regex_url,
        fill_regex_prompt,
        transform_model_name,
        transform_api_key,
        transform_url,
        transform_prompt,
        fill_regex_cot_sample_path,
        fill_regex_train_prompt,
        fill_regex_train_dataset_path,
        fill_regex_train_metric,
        fill_regex_train_metric_threshold,
        parser_dir,
        num_jobs
    )
    architecture(stage2_config)


if __name__ == "__main__":
    stage2(sys.argv[1])
