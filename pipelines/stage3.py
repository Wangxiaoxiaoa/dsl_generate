from src.tools.parser_yaml import parse_yaml
from src.tools.read_file import read_stage2_output
from src.tools.config_process import Stage3_Config, stage3_transform_server_config, stage3_io_related_config, stage3_control_config,stage3_dsl2nl_server_config, stage3_verify_server_config
from src.dspy.stage3_dsl2nl import dsl2nl
from src.dspy.stage3_verify import verify
from src.dspy.stage3_transform import transform
from tqdm import tqdm
from multiprocessing import Pool
import sys
from src.tools.save_file import save_file


def process(stage3_config, complete_sentence):
    for _ in range(Stage3_Config.dsl2nl_epochs):
        nl_sentence = dsl2nl(
            stage3_config.d2n_model_name,
            stage3_config.d2n_api_key,
            stage3_config.d2n_url,
            stage3_config.grammar,
            stage3_config.grammar_help,
            complete_sentence,
            stage3_config.roles_path,
            cot_sample=stage3_config.cot_sample_path,
            train_prompt=stage3_config.d2n_train_prompt,
            train_dataset_path=stage3_config.d2n_train_dataset_path
            )
        vertify_result = verify(
            stage3_config.v_model_name,
            stage3_config.v_api_key,
            stage3_config.v_url,
            stage3_config.v_prompt,
            nl_sentence
        )
        if vertify_result == "True":
            dsl_nl_pair = {
                "dsl": complete_sentence,
                "nl": nl_sentence
            }
            save_file(stage3_config.stage3_output_path, dsl_nl_pair, "a")
            break
        else:
            for _ in range(Stage3_Config.transform_epochs):
                transform_result = transform(
                    stage3_config.t_model_name,
                    stage3_config.t_api_key,
                    stage3_config.t_url,
                    stage3_config.t_prompt,
                    nl_sentence
                )
                vertify_result = verify(
                    stage3_config.v_model_name,
                    stage3_config.v_api_key,
                    stage3_config.v_url,
                    stage3_config.v_prompt,
                    transform_result
                )
                if vertify_result == "True":
                    dsl_nl_pair = {
                        "dsl": complete_sentence,
                        "nl": transform_result
                    }
                    save_file(stage3_config.stage3_output_path, dsl_nl_pair, "a")
                    break



def architecture(stage3_config):
    complete_sentence_list = read_stage2_output(stage3_config.stage2_output_path)
    with Pool(processes=stage3_config.num_jobs) as pool:
        list(tqdm(pool.imap(process, [(stage3_config, sentence) for sentence in complete_sentence_list]), total=len(complete_sentence_list)))


def stage3(config_path):
    config = parse_yaml(config_path)
    d2n_model_name, d2n_api_key, d2n_url, d2n_prompt, d2n_train_prompt, d2n_train_dataset_path, cot_sample_path = stage3_dsl2nl_server_config(config)
    v_model_name, v_api_key, v_url, v_prompt = stage3_verify_server_config(config)
    t_model_name, t_api_key, t_url, t_prompt = stage3_transform_server_config(config)
    grammar, grammar_help, stage2_output_path, stage3_output_path, roles_path = stage3_io_related_config(config)
    dsl2nl_epochs, transform_epochs, num_jobs = stage3_control_config(config)
    stage3_config = Stage3_Config(
        d2n_model_name,
        d2n_api_key, 
        d2n_url,
        d2n_prompt,
        d2n_train_prompt,
        d2n_train_dataset_path,
        v_model_name,
        v_api_key,
        v_url,
        v_prompt,
        t_model_name,
        t_api_key,
        t_url,
        t_prompt,
        grammar,
        grammar_help,
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