from grammarinator.runtime import RuleSize
from grammarinator.tool import DefaultPopulation, ParserTool
from grammarinator.cli import iter_files
import os
from os.path import exists, join
from multiprocessing import Pool

def parse_files(
    grammar_files,
    input_files=None,
    glob_patterns=None,
    rule=None,
    transformers=None,
    hidden=None,
    max_depth=RuleSize.max.depth,
    strict=False,
    out_dir=os.getcwd(),
    parser_dir=None,
    lib_dir=None,
    tree_extension='.tree',
    tree_codec='pickle',
    encoding='utf-8',
    encoding_errors='strict',
    cleanup=True,
    jobs=1,
    antlr='auto'
):
    """
    解析输入文件并生成语法树
    
    Args:
        grammar_files (list): ANTLR语法文件列表
        input_files (list, optional): 要处理的输入文件或目录列表
        glob_patterns (list, optional): 输入文件的通配符模式
        rule (str, optional): 开始解析的规则名称
        transformers (list, optional): 用于后处理解析树的转换器列表
        hidden (list, optional): 要构建到解析树中的隐藏token列表
        max_depth (int, optional): 最大预期树深度
        strict (bool, optional): 是否丢弃包含语法错误的测试
        out_dir (str, optional): 保存树的目录
        parser_dir (str, optional): 保存解析器语法的目录
        lib_dir (str, optional): 导入语法的替代位置
        tree_extension (str, optional): 树文件扩展名
        tree_codec (str, optional): 树编码格式
        encoding (str, optional): 输入文件编码
        encoding_errors (str, optional): 编码错误处理方式
        cleanup (bool, optional): 是否清理临时文件
        jobs (int, optional): 并行作业数
        antlr (str, optional): ANTLR工具路径
    """
    # 验证grammar文件是否存在
    for grammar in grammar_files:
        if not exists(grammar):
            raise ValueError(f'{grammar} does not exist.')

    if not parser_dir:
        parser_dir = join(out_dir, 'grammars')

    # 创建参数对象用于兼容原有代码
    class Args:
        pass
    
    args = Args()
    args.input = input_files or []
    args.glob = glob_patterns or []
    
    with ParserTool(
        grammars=grammar_files,
        hidden=hidden or [],
        transformers=transformers or [],
        parser_dir=parser_dir,
        antlr=antlr,
        rule=rule,
        population=DefaultPopulation(out_dir, tree_extension, codec=tree_codec),
        max_depth=max_depth,
        strict=strict,
        lib_dir=lib_dir,
        cleanup=cleanup,
        encoding=encoding,
        errors=encoding_errors
    ) as parser_tool:
        if jobs > 1:
            with Pool(jobs) as pool:
                for _ in pool.imap_unordered(parser_tool.parse, iter_files(args)):
                    pass
        else:
            for fn in iter_files(args):
                parser_tool.parse(fn)
