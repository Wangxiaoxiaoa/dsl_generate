from grammarinator.tool.parser import ParserTool
import logging
from antlr4 import InputStream, FileStream


logger = logging.getLogger(__name__)

class CFG_ParserTool(ParserTool):

    def parse(self, fn):
        """
        Load content from file, parse it to an ANTLR tree, convert it to
        Grammarinator tree, and save it to population.

        :param str fn: Path to the input file.
        """
        logger.info('Process file %s.', fn)
        try:
            root = self._create_tree(FileStream(fn, encoding=self._encoding, errors=self._errors), fn)
            if root is not None:
                self._population.add_individual(root, path=fn)
        except Exception as e:
            logger.warning('Exception while processing %s.', fn, exc_info=e)