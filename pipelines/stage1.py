# 标准库导入
import json
import os
import random
import sys
from argparse import Namespace
from functools import partial
from itertools import count
from math import inf
from multiprocessing import Manager, Pool

from grammarinator.generate import create_test
from grammarinator.runtime.rule import RuleSize
from grammarinator.tool import DefaultGeneratorFactory, DefaultPopulation
from inators.imp import import_object

from src.generate.generater import CFG_GeneratorTool
from src.process.processor import CFGProcessorTool
from src.tools.parser_yaml import parse_yaml
from src.parse.parse import build_grammars
from src.tools.logger import Logger

logger = Logger("stage1")

def process_grammar_programmatically(
    grammar_files,           
    output_dir='src/generate/cfg_generate/',         
    options={},             
    default_rule=None,      
    encoding='utf-8',       
    encoding_errors='strict', 
    lib_dir=None,           
    actions=True,           
    pep8=False,
    re_lexical_rules_special_token=None,
    re_lexical_rules=None
):

    processor = CFGProcessorTool('py', output_dir)    

    processor.process(
        grammars=grammar_files,
        options=options,
        default_rule=default_rule,
        encoding=encoding,
        errors=encoding_errors,
        lib_dir=lib_dir,
        actions=actions,
        pep8=pep8,
        re_lexical_rules_special_token=re_lexical_rules_special_token,
        re_lexical_rules=re_lexical_rules
    )

def generate_grammars(
    generator_path,  
    output_dir=None,  
    num_tests=1,  
    rule=None,  
    max_depth=None,  
    random_seed=None,  
    jobs=1  ,
    max_tokens=200
):

    args = Namespace(
        generator=generator_path,
        out_format=output_dir,
        n=num_tests,
        
        rule=rule,
        max_depth=max_depth,
        max_tokens=max_tokens,  
        random_seed=random_seed,
        jobs=jobs,
        
        model='grammarinator.runtime.DefaultModel',
        listener=[],
        transformer=[],
        serializer=None,
        weights=None,
        population=None,
        generate=True,
        mutate=True,
        recombine=True,
        unrestricted=True,
        keep_trees=False,
        dry_run=False,
        encoding='utf-8',
        encoding_errors='strict',
        tree_extension='.tree',
        tree_codec='json',
        tree_format='json'
    )


    args.generator = import_object(args.generator)
    args.model = import_object(args.model)
    args.listener = [import_object(listener) for listener in args.listener] if args.listener else []
    args.transformer = [import_object(transformer) for transformer in args.transformer] if args.transformer else []
    args.serializer = import_object(args.serializer) if args.serializer else None
   

    if args.weights:
        if not os.path.exists(args.weights):
            raise ValueError('Custom weights should point to an existing JSON file.')

        with open(args.weights, 'r') as f:
            weights = {}
            for rule, alts in json.load(f).items():
                for alternation_idx, alternatives in alts.items():
                    for alternative_idx, w in alternatives.items():
                        weights[(rule, int(alternation_idx), int(alternative_idx))] = w
            args.weights = weights

    if args.population:
        args.population = os.path.abspath(args.population)

    if args.random_seed is not None:
        random.seed(args.random_seed)

    def cfg_generator_tool_helper(args, lock=None):
        return CFG_GeneratorTool(generator_factory=DefaultGeneratorFactory(args.generator,
                                                                   model_class=args.model,
                                                                   weights=args.weights,
                                                                   listener_classes=args.listener),
                         rule=args.rule, out_format=args.out_format, lock=lock,
                         limit=RuleSize(depth=args.max_depth, tokens=args.max_tokens),
                         population=DefaultPopulation(args.population, args.tree_extension, args.tree_codec) if args.population else None,
                         generate=args.generate, mutate=args.mutate, recombine=args.recombine, unrestricted=args.unrestricted, keep_trees=args.keep_trees,
                         transformers=args.transformer, serializer=args.serializer,
                         cleanup=False, encoding=args.encoding, errors=args.encoding_errors, dry_run=args.dry_run)


    if args.jobs > 1:
        with Manager() as manager:
            with cfg_generator_tool_helper(args, lock=manager.Lock()) as generator_tool:
                parallel_create_test = partial(create_test, generator_tool, seed=args.random_seed)
                with Pool(args.jobs) as pool:
                    for _ in pool.imap_unordered(parallel_create_test, count(0) if args.n == inf else range(args.n)):
                        pass
    else:
        with cfg_generator_tool_helper(args) as generator_tool:
            for i in count(0) if args.n == inf else range(args.n):
                create_test(generator_tool, i, seed=args.random_seed)

def stage1(yaml_file):
    config = parse_yaml(yaml_file)
    logger.info(f"stage1 config: {config}")
    logger.info(f"begin to process grammar programmatically")
    process_grammar_programmatically(
        grammar_files=[config['grammar_path']] if isinstance(config['grammar_path'], str) else config['grammar_path'],
        default_rule=config['start_rule'],
        re_lexical_rules_special_token=config['re_lexical_rules_special_token'],
        re_lexical_rules = config['re_lexical_rules']
    )
    logger.info(f"begin to generate grammars")
    generate_grammars(
        generator_path='src.generate.cfg_generate.querylangGenerator.querylangGenerator',
        output_dir = config['output_dir'], 
        num_tests = config['num_samples'],
        rule = config['start_rule'],
        max_depth = config['max_depth'],
        random_seed = config['random_seed'],
        jobs = config['jobs'],
        max_tokens=config['max_tokens']
    )
    logger.info(f"begin to build grammars")
    build_grammars(config['grammar_path'], config['parser_dir'])

if __name__ == '__main__':
    config_file = sys.argv[1]
    stage1(config_file)