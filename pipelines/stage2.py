from src.tools.parser_yaml import parse_yaml
from src.tools.read_file import read_stage1_output
from src.tools.config_process import Stage2_Config, stage2_process_server_config, stage2_process_common_config, stage2_process_regex_config, stage2_process_control_config
from src.dspy.stage2_verfication_filter import verify
from src.dspy.stage2_fill_regex import fill_regex
from src.dspy.stage2_transform import transform
from tqdm import tqdm
from multiprocessing import Pool
import sys
from src.tools.save_file import save_file

def process(stage2_config, skeleton_sentence):
    verify_flag = verify(
        stage2_config.v_model_name, stage2_config.v_api_key, stage2_config.v_url,
        stage2_config.v_prompt, stage2_config.grammar_help, skeleton_sentence,
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
                error_msg=error_msg
            )
            verify_flag = verify(
                stage2_config.v_model_name, stage2_config.v_api_key, stage2_config.v_url,
                stage2_config.v_prompt, stage2_config.grammar_help, transform_sentence,
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
            stage2_config.fill_regex_max_retries, stage2_config.re_lexical_rules_special_token
        )
        if result_flag:
            save_file(stage2_config.stage2_output_path, complete_sentence, 'a')

def architecture(stage2_config):
    skeleton_sentence_list = read_stage1_output(stage2_config.stage1_output_path)
    with Pool(processes=stage2_config.num_jobs) as pool:
        list(tqdm(pool.imap(process, [(stage2_config, sentence) for sentence in skeleton_sentence_list]), total=len(skeleton_sentence_list)))

def stage2(config_path):
    config = parse_yaml(config_path)
    grammar, grammar_help, stage1_output_path, stage2_output_path = stage2_process_common_config(config)
    re_lexical_rules_special_token = stage2_process_regex_config(config)
    transform_epochs, fill_regex_max_retries = stage2_process_control_config(config)
    v_model_name, v_api_key, v_url, v_prompt = stage2_process_server_config(config, 'rationality_verification')
    fill_regex_model_name, fill_regex_api_key, fill_regex_url, fill_regex_prompt = stage2_process_server_config(config, 'fill_regex')
    transform_model_name, transform_api_key, transform_url, transform_prompt = stage2_process_server_config(config, 'transform')
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
        transform_prompt
    )
    architecture(stage2_config)


if __name__ == "__main__":
    stage2(sys.argv[1])
