from src.tools.read_file import read_file
from dataclasses import dataclass

def stage2_process_verify_config(config):
    model_name = config['verify']['model_name']
    api_key = config['verify']['api_key']
    url = config['verify']['url']
    prompt_path = config['verify']['prompt_path']
    prompt = read_file(prompt_path)
    return model_name, api_key, url, prompt

def stage2_process_transform_config(config):
    model_name = config['transform']['model_name']
    api_key = config['transform']['api_key']
    url = config['transform']['url']
    prompt_path = config['transform']['prompt_path']
    prompt = read_file(prompt_path)
    return model_name, api_key, url, prompt

def stage2_process_fill_regex_config(config):
    model_name = config['fill_regex']['model_name']
    api_key = config['fill_regex']['api_key']
    url = config['fill_regex']['url']
    prompt_path = config['fill_regex']['prompt_path']
    cot_sample_path = config['fill_regex']['cot_sample_path']
    train_prompt = config['fill_regex']['train_prompt']
    train_dataset_path = config['fill_regex']['train_dataset_path']
    train_metric = config['fill_regex']['train_metric']
    train_metric_threshold = config['fill_regex']['train_metric_threshold']
    parser_dir = config['fill_regex']['parser_dir']
    prompt = read_file(prompt_path)
    return model_name, api_key, url, prompt, cot_sample_path, train_prompt,train_dataset_path, train_metric, train_metric_threshold,parser_dir

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
    num_jobs = config['control']['num_jobs']
    return transform_epochs, fill_regex_max_retries, num_jobs


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
    fill_regex_cot_sample_path: str
    fill_regex_train_prompt: str
    fill_regex_train_dataset_path: str
    fill_regex_train_metric: str
    fill_regex_train_metric_threshold: float
    parser_dir: str
    num_jobs: int


def stage3_process_roles_config(config):
    return config['io_related']['roles_path']  # 直接返回路径

def stage3_dsl2nl_server_config(config):
    dsl = config['dsl2nl_server']
    return (dsl['model_name'],
            dsl['prompt_path'],  # 返回prompt路径
            dsl['api_key'],
            dsl['url'],
            dsl['cot_sample_path'],
            dsl['train_prompt'],
            dsl['train_dataset_path'],
            dsl['train_metric'],
            dsl['train_metric_threshold'])

def stage3_verify_server_config(config):
    verify = config['verify']
    return (verify['model_name'],
            verify['prompt_path'],  # 返回prompt路径
            verify['api_key'],
            verify['url'])

def stage3_transform_server_config(config):
    transform = config['transform']
    return (transform['model_name'],
            transform['prompt_path'],  # 返回prompt路径
            transform['api_key'],
            transform['url'])

def stage3_io_related_config(config):
    io = config['io_related']
    return (io['grammar_path'],  # 返回语法文件路径
            io['grammar_help_path'],  # 返回帮助文件路径
            io['stage2_output_path'],
            io['stage3_output_path'],
            io['roles_path'])

def stage3_control_config(config):
    control = config['control']
    return (control['dsl2nl_epochs'],
            control['transform_epochs'],
            control['num_jobs'])

@dataclass
class Stage3_Config:
    d2n_model_name: str
    d2n_prompt_path: str
    d2n_api_key: str
    d2n_url: str
    d2n_cot_sample_path: str
    d2n_train_prompt: str
    d2n_train_dataset_path: str
    d2n_train_metric: str
    d2n_train_metric_threshold: float
    v_model_name: str
    v_prompt_path: str
    v_api_key: str
    v_url: str
    t_model_name: str
    t_prompt_path: str
    t_api_key: str
    t_url: str
    grammar_path: str
    grammar_help_path: str
    stage2_output_path: str
    stage3_output_path: str
    roles_path: str
    dsl2nl_epochs: int
    transform_epochs: int
    num_jobs: int