import os
from argparse import Namespace
from math import inf
from multiprocessing import Pool
from os.path import exists, join

from antlerinator import process_antlr_argument
from grammarinator.cli import iter_files, logger, process_tree_format_argument
from grammarinator.runtime import RuleSize
from grammarinator.tool import DefaultPopulation, ParserTool
from inators.arg import process_log_level_argument, process_sys_path_argument, process_sys_recursion_limit_argument
import sys
import yaml

def process_config(config):

    grammars = [config['grammar_path']] if isinstance(config['grammar_path'], str) else config['grammar_path']
    for grammar in grammars:
        if not exists(grammar):
            raise ValueError(f'{grammar} does not exist.')

    if 'parser_dir' not in config or not config['parser_dir']:
        config['parser_dir'] = join(config['output_path'], 'grammars')

    return config

def cfg_parser(config):
    try:
        config = process_config(config)
    except ValueError as e:
        print(f"错误: {e}")
        sys.exit(1)

    args = Namespace(
        grammar=[config['grammar_path']] if isinstance(config['grammar_path'], str) else config['grammar_path'],
        input=config['input_path'],
        glob=None,
        rule=config.get('rule', None),  # 使用get方法设置默认值
        transformer=config.get('transformer', []),
        hidden=config.get('hidden', []),
        max_depth=config.get('max_depth', inf),
        strict=config.get('strict', False),
        parser_dir=config['parser_dir'],
        out=config['output_path'],
        lib=config.get('lib', None),
        tree_format=config.get('tree_format', 'json'),
        tree_codec=config.get('tree_codec', 'json'),
        tree_extension=config.get('tree_extension', '.tree'),
        cleanup=config.get('cleanup', True),
        jobs=config.get('jobs', 1),
        encoding=config.get('encoding', 'utf-8'),
        encoding_errors=config.get('encoding_errors', 'strict'),
        antlr=config.get('antlr', '4.13.0'),
        sys_path=config.get('sys_path', []),
        sys_recursion_limit=config.get('sys_recursion_limit', None),
        log_level=config.get('log_level', None),
    )

    process_sys_path_argument(args)
    process_sys_recursion_limit_argument(args)
    process_antlr_argument(args)
    process_tree_format_argument(args)
    if args.log_level:
        process_log_level_argument(args, logger)

    with ParserTool(grammars=args.grammar, 
                   hidden=args.hidden, 
                   transformers=args.transformer, 
                   parser_dir=args.parser_dir, 
                   antlr=args.antlr, 
                   rule=args.rule,
                   population=DefaultPopulation(args.out, args.tree_extension, codec=args.tree_codec), 
                   max_depth=args.max_depth, 
                   strict=args.strict,
                   lib_dir=args.lib, 
                   cleanup=args.cleanup, 
                   encoding=args.encoding, 
                   errors=args.encoding_errors) as parser_tool:
        
        if args.jobs > 1:
            with Pool(args.jobs) as pool:
                for _ in pool.imap_unordered(parser_tool.parse, iter_files(args)):
                    pass
        else:
            for fn in iter_files(args):
                parser_tool.parse(fn)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("用法: python parser_demo.py config.yaml")
        sys.exit(1)

    config_file = sys.argv[1]
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        cfg_parser(config)
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)