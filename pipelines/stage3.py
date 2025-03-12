from src.tools.parser_yaml import parse_yaml
from src.tools.read_file import read_stage2_output
from src.tools.config_process import Stage3_Config, stage3_transform_server_config, stage3_io_related_config, stage3_control_config,stage3_dsl2nl_server_config, stage3_verify_server_config
from src.dspy.stage3_dsl2nl import dsl2nl
from src.dspy.stage3_verify import verify
from src.dspy.stage3_transform import transform
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor  
import sys
import dspy
from src.tools.save_file import save_file
from src.tools.logger import Logger

logger = Logger("stage2")

def process(config_sentence_pair):
    stage3_config, complete_sentence = config_sentence_pair
    for _ in range(stage3_config.dsl2nl_epochs):
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
        if verify_result == True:
            dsl_nl_pair = {
                "nl": nl_sentence,
                "dsl": complete_sentence
            }
            save_file(stage3_config.stage3_output_path, dsl_nl_pair, "a")
            break
        else:
            for _ in range(stage3_config.transform_epochs):
                transform_nl = transform(
                    stage3_config.t_model_name,
                    stage3_config.t_api_key,
                    stage3_config.t_url,
                    stage3_config.grammar_path,
                    stage3_config.grammar_help_path,
                    complete_sentence,
                    nl_sentence
                )
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
                if verify_result == True:
                    dsl_nl_pair = {
                        "dsl": complete_sentence,
                        "nl": transform_nl
                    }
                    save_file(stage3_config.stage3_output_path, dsl_nl_pair, "a")
                    break

def architecture(stage3_config):
    complete_sentence_list = read_stage2_output(stage3_config.stage2_output_path)
    model_name = "openai/" + stage3_config.d2n_model_name
    llm = dspy.LM(model_name, api_key=stage3_config.d2n_api_key, api_base=stage3_config.d2n_url)
    dspy.configure(lm=llm)
    with ThreadPoolExecutor(max_workers=stage3_config.num_jobs) as executor:
        tasks = [(stage3_config, sentence) for sentence in complete_sentence_list]
        list(tqdm(executor.map(process, tasks), total=len(complete_sentence_list)))


def stage3(config_path):
    config = parse_yaml(config_path)
    
    (d2n_model_name,
     d2n_prompt_path,  
     d2n_api_key,
     d2n_url,
     d2n_cot_sample_path,
     d2n_train_prompt,
     d2n_train_dataset_path,
     d2n_train_metric,
     d2n_train_metric_threshold) = stage3_dsl2nl_server_config(config)  
   
    (v_model_name,
     v_prompt_path,  
     v_api_key,
     v_url) = stage3_verify_server_config(config)
    
    (t_model_name,
    t_prompt_path,  
    t_api_key,
    t_url) = stage3_transform_server_config(config)
    
    (grammar_path,
     grammar_help_path,
     stage2_output_path,
     stage3_output_path,
     roles_path) = stage3_io_related_config(config)
    
    (dsl2nl_epochs,
     transform_epochs,
     num_jobs) = stage3_control_config(config)
    

    stage3_config = Stage3_Config(
        d2n_model_name,
        d2n_prompt_path,
        d2n_api_key,
        d2n_url,
        d2n_cot_sample_path,
        d2n_train_prompt,
        d2n_train_dataset_path,
        d2n_train_metric,
        d2n_train_metric_threshold,
        v_model_name,
        v_prompt_path,
        v_api_key,
        v_url,
        t_model_name,
        t_prompt_path,
        t_api_key,
        t_url,
        grammar_path,
        grammar_help_path,
        stage2_output_path,
        stage3_output_path,
        roles_path,
        dsl2nl_epochs,
        transform_epochs,
        num_jobs
    )
    architecture(stage3_config)


if __name__ == "__main__":
    config = sys.argv[1]
    stage3(config)