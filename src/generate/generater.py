import codecs
from grammarinator.runtime.generator import (Generator,  QuantifierContext, QuantifiedContext, 
                                          AlternationContext, UnparserRuleContext, UnlexerRuleContext, RuleContext, UnlexerRule)
from grammarinator.tool.generator import GeneratorTool
from grammarinator.runtime.rule import RuleSize


class CFG_UnlexerRuleContext(RuleContext):

    __slots__ = ('_start_depth', '_parent_name', '_name')

    def __init__(self, gen, name, parent=None, immutable=False):
        if isinstance(parent, UnlexerRule):

            super().__init__(gen, parent)
            self._start_depth = None
            self._parent_name = parent.name
            self._name = name
        else:
            node = UnlexerRule(name=name, immutable=immutable)
            if parent:
                parent += node
            super().__init__(gen, node)
            self._start_depth = self.gen._size.depth
            self._parent_name = None
            self._name = name

    def __enter__(self):

        if self._name is not None and self._parent_name is not None:
            self.node.name = self._name
        super().__enter__()
        self.gen._size.tokens += 1
        self.node.size.tokens += 1
        self.node.size.depth = max(self.node.size.depth, self.gen._size.depth)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)
        if self._start_depth is not None:
            self.node.size.depth -= self._start_depth
        if self._name is not None and self._parent_name is not None:
            self.node.name = self._parent_name


class CFG_UnparserRuleContext(UnparserRuleContext):
    def __init__(self, gen, name, parent=None):
        super().__init__(gen, name, parent)
        self._name = name


class CFG_QuantifierContext(QuantifierContext):

    def __call__(self,name,lexicals):
        keys = []
        if lexicals:
            for item in lexicals:
                if list(item.keys())[0] not in keys:
                    keys.append(list(item.keys())[0])
                else:
                    continue
        if name in keys and self._cnt == 0:
            self._cnt += 1
            return True
        else:
            if self._cnt < self._start:
                self._cnt += 1
                return True

            gen = self._rule.gen
            if (self._cnt < self._stop
                    and gen._size + self._min_size <= gen._limit
                    and gen._model.quantify(self._rule.node, self.idx, self._cnt, self._start, self._stop)):
                self._cnt += 1
                return True

            return False


class CFG_GeneratorTool(GeneratorTool):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def create_test(self,index):
        root = self.create()
        test = self._serializer(root)
        if self._dry_run:
            return None
        output_dir = self._out_format
        if self._population is not None and self._keep_trees:
            self._population.add_individual(root, path=output_dir)

        if output_dir:
            with codecs.open(output_dir, 'a+', self._encoding, self._errors) as f:
                f.write(test+'\n')
        else:
            with self._lock:
                print(test)

