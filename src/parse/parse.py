from grammarinator.tool.parser import ParserTool,ExtendedErrorListener,CommonTokenStream,logger
from antlr4 import InputStream
from os.path import basename, commonprefix, split, splitext
from subprocess import CalledProcessError, PIPE, run
from antlerinator import default_antlr_jar_path, __antlr_version__, download
import sys
import os

class CFG_ParserTool():

    def __init__(self,grammar, parser_dir):
        self.grammar = grammar
        self.parser_dir = parser_dir
        self.lexer_cls, self.parser_cls, self.listener_cls = self._build_parser(parser_dir)


    def _build_parser(self, parser_dir):
        try:
            languages = {
                'python': {'antlr_arg': '-Dlanguage=Python3',
                           'ext': 'py',
                           'listener_format': 'Listener'}
            }

            def file_endswith(end_pattern):
                files = os.listdir(parser_dir)
                matching_files = [f for f in files if f.endswith(end_pattern)]
                if not matching_files:
                    raise ValueError(f"No files found ending with {end_pattern}")
                return os.path.splitext(matching_files[0])[0]
            
            lexer = file_endswith(f'Lexer.{languages["python"]["ext"]}')
            parser = file_endswith(f'Parser.{languages["python"]["ext"]}')
            listener = file_endswith(f'{languages["python"]["listener_format"]}.{languages["python"]["ext"]}')

            if parser_dir not in sys.path:
                sys.path.append(parser_dir)

            return (getattr(__import__(x, globals(), locals(), [x], 0), x) for x in [lexer, parser, listener])
        except Exception as e:
            logger.error('Exception while loading parser modules', exc_info=e)
            raise

    def _create_tree(self, input_stream):
        try:
            lexer = self.lexer_cls(input_stream)
            lexer.addErrorListener(ExtendedErrorListener())
            parser = self.parser_cls(CommonTokenStream(lexer))
            if parser._syntaxErrors:
                return False
            return True
        except:
            return False
   
    def parse(self,dsl_text):
        parser_result = self._create_tree(InputStream(dsl_text))
        return parser_result
    

def build_grammars(grammar_path, parser_dir):
    if not os.path.exists(parser_dir):
        os.makedirs(parser_dir)
    
    if not os.path.isabs(grammar_path):
        grammar_path = os.path.abspath(grammar_path)
    try:
        download()        
    except Exception as e:
        print(f"downloading ANTLR jar file: {e}")
    antlr = default_antlr_jar_path(__antlr_version__)
    try:
        cmd = ["java", "-jar", antlr, "-Dlanguage=Python3", "-o", parser_dir, grammar_path]       
        result = run(cmd, stdout=PIPE, stderr=PIPE, check=True)         
        if not result.stdout and not result.stderr:
            print("Warning: ANTLR command produced no output")
            if os.path.exists(parser_dir):
                generated_files = os.listdir(parser_dir)
                print(f"Files in parser directory: {generated_files}")
            else:
                print(f"Parser directory does not exist: {parser_dir}")
            
    except CalledProcessError as e:
        logger.error('Building grammars %r failed!\n%s\n%s\n', grammar_path,
                    e.stdout.decode('utf-8', 'ignore'),
                    e.stderr.decode('utf-8', 'ignore'))
        raise