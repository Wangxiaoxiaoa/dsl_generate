from src.tools.read_file import read_file
from dataclasses import dataclass

def stage2_process_server_config(config, server_name):
    model_name = config[server_name]['model_name']
    api_key = config[server_name]['api_key']
    url = config[server_name]['url']
    prompt_path = config[server_name]['prompt_path']
    prompt = read_file(prompt_path)
    return model_name, api_key, url, prompt

def stage2_process_common_config(config):
    grammar_path = config['io_related']['grammar_path']
    grammar_help_path = config['io_related']['grammar_help_path']
    stage1_output_path = config['io_related']['stage1_output_path']
    stage2_output_path = config['io_related']['stage2_output_path']
    grammar = read_file(grammar_path)
    grammar_help = read_file(grammar_help_path)
    return grammar, grammar_help, stage1_output_path, stage2_output_path

def stage2_process_regex_config(config):
    re_lexical_rules_special_token = config['regex_related']['re_lexical_rules_special_token']
    return re_lexical_rules_special_token


def stage2_process_control_config(config):
    transform_epochs = config['control']['transform_epochs']
    fill_regex_max_retries = config['control']['fill_regex_max_retries']
    return transform_epochs, fill_regex_max_retries


@dataclass
class Stage2_Config:
    grammar: str
    grammar_help: str
    stage1_output_path: str
    stage2_output_path: str
    re_lexical_rules_special_token: list
    transform_epochs: int
    fill_regex_max_retries: int
    v_model_name: str
    v_api_key: str
    v_url: str
    v_prompt: str
    fill_regex_model_name: str
    fill_regex_api_key: str
    fill_regex_url: str
    fill_regex_prompt: str
    transform_model_name: str
    transform_api_key: str
    transform_url: str
    transform_prompt: str



def stage3_process_roles_config(config):
    roles_path = config['io_related']['roles_path']
    roles = read_file(roles_path)
    return roles

def stage3_dsl2nl_server_config(config):
    model_name = config['dsl2nl_server']['model_name']
    prompt_path = config['dsl2nl_server']['prompt_path']
    api_key = config['dsl2nl_server']['api_key']
    url = config['dsl2nl_server']['url']
    train_prompt = config['dsl2nl_server']['train_prompt']
    train_dataset_path = config['dsl2nl_server']['train_dataset_path']
    cot_sample_path = config['dsl2nl_server']['cot_sample_path']
    prompt = read_file(prompt_path)
    if train_prompt:
        train_dataset = read_file(train_dataset_path)
    return model_name, api_key, url, prompt, train_prompt, train_dataset, cot_sample_path

def stage3_verify_server_config(config):
    model_name = config['verify']['model_name']
    prompt_path = config['verify']['prompt_path']
    api_key = config['verify']['api_key']
    url = config['verify']['url']
    prompt = read_file(prompt_path)
    return model_name, api_key, url, prompt

def stage3_transform_server_config(config):
    model_name = config['transform']['model_name']
    prompt_path = config['transform']['prompt_path']
    api_key = config['transform']['api_key']
    url = config['transform']['url']
    prompt = read_file(prompt_path)
    return model_name, api_key, url, prompt

def stage3_io_related_config(config):
    grammar_path = config['io_related']['grammar_path']
    grammar_help_path = config['io_related']['grammar_help_path']
    stage2_output_path = config['io_related']['stage2_output_path']
    stage3_output_path = config['io_related']['stage3_output_path']
    roles_path = config['io_related']['roles_path']
    grammar = read_file(grammar_path)
    grammar_help = read_file(grammar_help_path)
    return grammar, grammar_help, stage2_output_path, stage3_output_path, roles_path

def stage3_control_config(config):
    dsl2nl_epochs = config['control']['dsl2nl_epochs']
    transform_epochs = config['control']['transform_epochs']
    num_jobs = config['control']['num_jobs']
    return dsl2nl_epochs, transform_epochs, num_jobs

@dataclass
class Stage3_Config:
    cot_sample_path: str
    d2n_model_name: str
    d2n_prompt_path: str
    d2n_api_key: str
    d2n_url: str
    d2n_prompt: str
    d2n_train_prompt: str
    d2n_train_dataset_path: str
    v_model_name: str
    v_prompt_path: str
    v_api_key: str
    v_url: str
    v_prompt: str
    t_model_name: str
    t_prompt_path: str
    t_api_key: str
    t_url: str
    t_prompt: str
    t_epochs: int
    grammar: str
    grammar_help: str
    stage2_output_path: str
    stage3_output_path: str
    roles_path: str
    dsl2nl_epochs: int
    transform_epochs: int
    num_jobs: int