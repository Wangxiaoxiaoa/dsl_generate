from grammarinator.tool.processor import (
    ProcessorTool,
    GrammarGraph,
    dot_ranges,
    append_unique,
    VariableNode,
    AlternativeNode,
    ActionNode,
    AlternationNode,
    LiteralNode,
    QuantifierNode,
    UnparserRuleNode,
    LambdaNode,
    ImagRuleNode,
    CharsetNode,
    UnlexerRuleNode,
    ANTLRv4Parser,
    multirange_diff,
    escape_string
)
from os.path import  join
from collections import Counter
from sys import maxunicode
import regex as re
import autopep8
from importlib import metadata
from os import getcwd
from jinja2 import Environment
from pkgutil import get_data

# __version__ = metadata.version(__package__)
from antlr4 import ParserRuleContext

class CFGGrammarGraph(GrammarGraph):       
    def __init__(self):
        self.lexicals = {}
        super().__init__()

    

class CFGProcessorTool(ProcessorTool):
    def __init__(self,lang, work_dir=None):
        self._lang = lang
        env = Environment(trim_blocks=True,
                          lstrip_blocks=True,
                          keep_trailing_newline=False)
        env.filters['substitute'] = lambda s, frm, to: re.sub(frm, to, str(s))
        env.filters['escape_string'] = escape_string   
          
        self._template = env.from_string(self.read_template("src/process/Jinja/GeneratorTemplate.py.jinja"))
        self._work_dir = work_dir or getcwd()

    def read_template(self,path):
        with open(path,'r',encoding='utf-8') as f:
            return f.read()

    def process(self, grammars, *, options=None, default_rule=None, encoding='utf-8', errors='strict', lib_dir=None, actions=True, pep8=False,re_lexical_rules_special_token=None,re_lexical_rules=None):

        lexer_root, parser_root = CFGProcessorTool.parse_grammars(grammars, self._work_dir, encoding, errors, lib_dir)
        graph = CFGProcessorTool.build_graph(actions, lexer_root, parser_root, options, default_rule,re_lexical_rules_special_token,re_lexical_rules)
        CFGProcessorTool._analyze_graph(graph)

        src = self._template.render(graph=graph).lstrip()
        with open(join(self._work_dir, graph.name + '.' + self._lang), 'w') as f:
            if pep8:
                src = autopep8.fix_code(src)
            f.write(src)

    @staticmethod
    def build_graph(actions, lexer_root, parser_root, options, default_rule,re_lexical_rules_special_token,re_lexical_rules):
        def find_conditions(node):
            if not actions:
                return '1'

            if isinstance(node, str):
                return node

            action_block = getattr(node, 'actionBlock', None)
            if action_block:
                if action_block() and action_block().ACTION_CONTENT() and node.QUESTION():
                    return ''.join(str(child) for child in action_block().ACTION_CONTENT())
                return '1'

            element = getattr(node, 'element', None) or getattr(node, 'lexerElement', None)
            if element:
                if not element():
                    return '1'
                return find_conditions(element(0))

            child_ref = getattr(node, 'alternative', None) or getattr(node, 'lexerElements', None)

            if not child_ref:
                return '1'

            return find_conditions(child_ref())

        def character_range_interval(node):
            start = str(node.characterRange().STRING_LITERAL(0))[1:-1]
            end = str(node.characterRange().STRING_LITERAL(1))[1:-1]
            start_cp, start_offset = process_lexer_char(start, 0, 'character range')
            end_cp, end_offset = process_lexer_char(end, 0, 'character range')

            if start_offset < len(start) or end_offset < len(end):
                raise ValueError(f'Only single characters are allowed in character ranges ({start!r}..{end!r})')

            return start_cp, end_cp + 1

        def process_lexer_char(s, offset, use_case):

            if s[offset] != '\\':
                return ord(s[offset]), offset + 1

            if offset + 2 > len(s):
                raise ValueError('Escape must have at least two characters')

            escaped = s[offset + 1]
            offset += 2 

            if escaped == 'u':
                if s[offset] == '{':
                    hex_start_offset = offset + 1
                    hex_end_offset = s.find('}', hex_start_offset)
                    if hex_end_offset == -1:
                        raise ValueError(f'Missing closing bracket for unicode escape ({s})')
                    if hex_start_offset == hex_end_offset:
                        raise ValueError(f'Missing codepoint for unicode escape ({s})')

                    offset = hex_end_offset + 1  # Skip over last bracket
                else:
                    hex_start_offset = offset
                    hex_end_offset = hex_start_offset + 4
                    if hex_end_offset > len(s):
                        raise ValueError(f'Non-bracketed unicode escape must be of form \\uXXXX ({s})')

                    offset = hex_end_offset

                try:
                    codepoint = int(s[hex_start_offset:hex_end_offset], 16)
                except ValueError as exc:
                    raise ValueError(f'Invalid hex value ({s})') from exc

                if codepoint < 0 or codepoint > maxunicode:
                    raise ValueError(f'Invalid unicode codepoint ({s})')

                return codepoint, offset

            if escaped in ('p', 'P'):
                if use_case != 'lexer charset':
                    raise ValueError(f'Unicode properties are allowed in lexer charsets only (not in {use_case})')

                if s[offset] != '{':
                    raise ValueError(f'Unicode properties must use the format: `\\p{{...}}` ({s})')

                prop_start_offset = offset + 1
                prop_end_offset = s.find('}', prop_start_offset)
                if prop_end_offset == -1:
                    raise ValueError(f'Missing closing bracket for unicode property escape ({s})')
                if prop_start_offset == prop_end_offset:
                    raise ValueError(f'Missing property name for unicode property escape ({s})')

                offset = prop_end_offset + 1  # Skip over last bracket

                def _name_to_codepoints(uni_prop):
                    try:
                        pattern = re.compile(uni_prop)
                    except Exception as e:
                        raise ValueError(f'Unknown property: {uni_prop}') from e
                    return [cp for cp in range(maxunicode) if pattern.match(chr(cp))]

                def _codepoints_to_ranges(codepoints):
                    ranges = []
                    start, current = None, None
                    last_cp_id = len(codepoints) - 1
                    for i, code in enumerate(codepoints):
                        if not start:
                            start = current = code
                        elif code == current + 1:
                            current = code
                            if i == last_cp_id:
                                ranges.append((start, current + 1))
                        else:
                            ranges.append((start, current + 1))
                            start = current = code
                    return ranges

                prop_name = s[prop_start_offset:prop_end_offset]


                if prop_name in ['Extended_Pictographic', 'EP']:
                    ranges = [(0x2388, 0x2389), (0x2605, 0x2606), (0x2607, 0x260d), (0x260f, 0x2610), (0x2612, 0x2613), (0x2616, 0x2617), (0x2619, 0x261c), (0x261e, 0x261f), (0x2621, 0x2622), (0x2624, 0x2625), (0x2627, 0x2629), (0x262b, 0x262d), (0x2630, 0x2637), (0x263b, 0x2647), (0x2654, 0x265f), (0x2661, 0x2662), (0x2664, 0x2665), (0x2667, 0x2668), (0x2669, 0x267a), (0x267c, 0x267e), (0x2680, 0x2691), (0x2695, 0x2696), (0x2698, 0x2699), (0x269a, 0x269b), (0x269d, 0x269f), (0x26a2, 0x26a9), (0x26ac, 0x26af), (0x26b2, 0x26bc), (0x26bf, 0x26c3), (0x26c6, 0x26c7), (0x26c9, 0x26cd), (0x26d0, 0x26d1), (0x26d2, 0x26d3), (0x26d5, 0x26e8), (0x26eb, 0x26ef), (0x26f6, 0x26f7), (0x26fb, 0x26fc), (0x26fe, 0x26ff), (0x2700, 0x2701), (0x2703, 0x2704), (0x270e, 0x270f), (0x2710, 0x2711), (0x2765, 0x2767), (0x1f000, 0x1f003), (0x1f005, 0x1f02b), (0x1f02c, 0x1f02f), (0x1f030, 0x1f093), (0x1f094, 0x1f09f), (0x1f0a0, 0x1f0ae), (0x1f0af, 0x1f0b0), (0x1f0b1, 0x1f0bf), (0x1f0c0, 0x1f0c1), (0x1f0c1, 0x1f0cf), (0x1f0d0, 0x1f0d1), (0x1f0d1, 0x1f0f5), (0x1f0f6, 0x1f0ff), (0x1f10d, 0x1f10f), (0x1f12f, 0x1f130), (0x1f16c, 0x1f16f), (0x1f1ad, 0x1f1e5), (0x1f203, 0x1f20f), (0x1f23c, 0x1f23f), (0x1f249, 0x1f24f), (0x1f252, 0x1f25f), (0x1f260, 0x1f265), (0x1f266, 0x1f2ff), (0x1f322, 0x1f323), (0x1f394, 0x1f395), (0x1f398, 0x1f399), (0x1f39c, 0x1f39d), (0x1f3f1, 0x1f3f2), (0x1f3f6, 0x1f3f7), (0x1f4fe, 0x1f4ff), (0x1f53e, 0x1f548), (0x1f54f, 0x1f550), (0x1f568, 0x1f56e), (0x1f571, 0x1f572), (0x1f57b, 0x1f586), (0x1f588, 0x1f589), (0x1f58e, 0x1f58f), (0x1f591, 0x1f594), (0x1f597, 0x1f5a3), (0x1f5a6, 0x1f5a7), (0x1f5a9, 0x1f5b0), (0x1f5b3, 0x1f5bb), (0x1f5bd, 0x1f5c1), (0x1f5c5, 0x1f5d0), (0x1f5d4, 0x1f5db), (0x1f5df, 0x1f5e0), (0x1f5e2, 0x1f5e3), (0x1f5e4, 0x1f5e7), (0x1f5e9, 0x1f5ee), (0x1f5f0, 0x1f5f2), (0x1f5f4, 0x1f5f9), (0x1f6c6, 0x1f6ca), (0x1f6d3, 0x1f6d4), (0x1f6d5, 0x1f6df), (0x1f6e6, 0x1f6e8), (0x1f6ea, 0x1f6eb), (0x1f6ed, 0x1f6ef), (0x1f6f1, 0x1f6f2), (0x1f6f7, 0x1f6f8), (0x1f6f9, 0x1f6ff), (0x1f774, 0x1f77f), (0x1f7d5, 0x1f7ff), (0x1f80c, 0x1f80f), (0x1f848, 0x1f84f), (0x1f85a, 0x1f85f), (0x1f888, 0x1f88f), (0x1f8ae, 0x1f8ff), (0x1f900, 0x1f90b), (0x1f90c, 0x1f90f), (0x1f91f, 0x1f920), (0x1f928, 0x1f92f), (0x1f931, 0x1f932), (0x1f93f, 0x1f940), (0x1f94c, 0x1f94d), (0x1f94d, 0x1f94f), (0x1f95f, 0x1f96b), (0x1f96c, 0x1f97f), (0x1f992, 0x1f997), (0x1f998, 0x1f9bf), (0x1f9c1, 0x1f9cf), (0x1f9d0, 0x1f9e6), (0x1f9e7, 0x1f9ff), (0x1fa00, 0x1fffd)]
                    return ranges if escaped == 'p' else multirange_diff(graph.charsets[dot_charset], ranges), offset

                codepoints = None
                if prop_name in ['EmojiRK', 'EmojiNRK']:
                    emoji_rk_codepoints = _name_to_codepoints(r'\p{GCB=Regional_Indicator}')
                    emoji_rk_codepoints.extend([ord(c) for c in ['*', '#', '\u00a9', '\u00ae', '\u2122', '\u3030', '\u303d'] + list(map(str, range(10)))])
                    if prop_name == 'EmojiRK':
                        codepoints = emoji_rk_codepoints
                    else:
                        codepoints = set(_name_to_codepoints(r'\p{Emoji=Yes}')) - set(emoji_rk_codepoints)
                elif prop_name == 'EmojiPresentation=EmojiDefault':
                    codepoints = set(_name_to_codepoints(r'\p{Emoji=Yes}')) & set(_name_to_codepoints(r'\p{Emoji_Presentation=Yes}'))
                elif prop_name == 'EmojiPresentation=TextDefault':
                    codepoints = set(_name_to_codepoints(r'\p{Emoji=Yes}')) & set(_name_to_codepoints(r'\p{Emoji_Presentation=No}'))
                elif prop_name == 'EmojiPresentation=Text':
                    codepoints = _name_to_codepoints(r'\p{Emoji=No}')

                if codepoints:
                    ranges = _codepoints_to_ranges(codepoints)
                    return ranges if escaped == 'p' else multirange_diff(graph.charsets[dot_charset], ranges), offset

                return _codepoints_to_ranges(_name_to_codepoints(f'\\{escaped}{{{prop_name}}}')), offset

            escaped_values = {
                'n': '\n',
                'r': '\r',
                'b': '\b',
                't': '\t',
                'f': '\f',
                '\\': '\\',
                '-': '-',
                ']': ']',
                '\'': '\''
            }

            if escaped in escaped_values:
                return ord(escaped_values[escaped]), offset

            raise ValueError('Invalid escaped value')

        def lexer_charset_interval(s):
            assert len(s) > 0, 'Charset cannot be empty'

            ranges = []

            offset = 0
            while offset < len(s):
                in_range = s[offset] == '-' and offset != 0 and offset != len(s) - 1
                if in_range:
                    offset += 1

                codepoint, offset = process_lexer_char(s, offset, 'lexer charset')

                if isinstance(codepoint, list):
                    if in_range or (offset < len(s) - 1 and s[offset] == '-'):
                        raise ValueError(f'Unicode property escapes are not allowed in lexer charset range ({s})')
                    ranges.extend(codepoint)
                elif in_range:
                    ranges[-1] = (ranges[-1][0], codepoint + 1)
                else:
                    ranges.append((codepoint, codepoint + 1))

            return ranges

        def chars_from_set(node):
            if node.characterRange():
                return [character_range_interval(node)]

            if node.LEXER_CHAR_SET():
                return lexer_charset_interval(str(node.LEXER_CHAR_SET())[1:-1])

            if node.STRING_LITERAL():
                char = str(node.STRING_LITERAL())[1:-1]
                char_cp, char_offset = process_lexer_char(char, 0, 'not set literal')
                if char_offset < len(char):
                    raise ValueError(f'Zero or multi-character literals are not allowed in lexer sets: {char!r}')
                return [(char_cp, char_cp + 1)]

            if node.TOKEN_REF():
                src = str(node.TOKEN_REF())
                assert graph.vertices[src].start_ranges is not None, f'{src} has no character start ranges.'
                return graph.vertices[src].start_ranges

            return []

        def unique_charset(ranges):
            if not ranges:
                raise ValueError('Charset must contain at least one range')
            for start, end in ranges:
                if end <= start:
                    raise ValueError(f"Charset range must not be empty: '\\u{{{start:x}}}'..'\\u{{{end - 1:x}}}', '{chr(start)}'..'{chr(end - 1)}'")

            return append_unique(graph.charsets, ranges)

        def unescape_string(s):
            def _iter_unescaped_chars(s):
                offset = 0
                while offset < len(s):
                    codepoint, offset = process_lexer_char(s, offset, 'string literal')
                    yield chr(codepoint)

            return ''.join(c for c in _iter_unescaped_chars(s))

        def parse_arg_action_block(node, use_case):
            args = []

            def _save_pair(k, v):
                if use_case != 'call' and k is None:
                    k, v = v, None
                t = None
                if k:
                    m = re.fullmatch(r'(\w+)\s*:([^:].*)', k)  
                    if m:
                        t, k = m.group(2, 1)
                        t = t.strip()
                    else:
                        m = re.fullmatch(r'(.+)\s+(\w+)', k)  
                        if m:
                            t, k = m.group(1, 2)
                            t = t.strip()
                        else:
                            m = re.fullmatch(r'(\w+)', k)  
                            if not m:
                                raise ValueError(f'unsupported type notation {k} in {use_case}')
                if t == '':
                    raise ValueError(f'type in {use_case} must not be empty')
                if k == '':
                    raise ValueError(f'name in {use_case} must not be empty')
                if v == '':
                    raise ValueError(f'value in {use_case} must not be empty')
                args.append((t, k, v))

            if node and node.argActionBlock():
                src = ''.join(str(chr_arg) for chr_arg in node.argActionBlock().ARGUMENT_CONTENT()).strip()
                pairs = Counter()
                start, offset, end = 0, 0, len(src)
                lhs = None
                while offset < end:
                    c = src[offset]
                    if c in ['\'', '"']:
                        offset += 1
                        while offset < end and src[offset] != c:
                            if src[offset] == '\\' and offset + 1 < end and src[offset + 1] == c:
                                offset += 1  
                            offset += 1  
                    elif c in ['(', '[', '{']:
                        pairs[c] += 1
                    elif c in [')', ']', '}']:
                        pairs[c] -= 1
                    elif c == ',':
                        if sum(pairs.values()) == 0:
                            _save_pair(lhs, src[start:offset].strip())
                            start = offset + 1
                            lhs = None
                    elif offset < end - 1 and src[offset:offset + 2] in ['==', '!=', '<=', '>=', '+=', '-=', '*=', '/=', '%=', '^=', ':=']:
                        offset += 1
                    elif c == '=' and lhs is None:
                        lhs = src[start:offset].strip()
                        start = offset + 1
                    offset += 1

                if sum(pairs.values()) != 0:
                    raise ValueError(f'Non-matching pairs in action ({",".join((k for k, v in pairs if v > 0))})')

                _save_pair(lhs, src[start:].strip())
            return args

        def isfloat(s):
            try:
                float(s)
                return True
            except ValueError:
                return False

        def build_rule(rule, node):
            lexer_rule = isinstance(rule, UnlexerRuleNode)
            def build_expr(node, parent_id):
                if isinstance(node, ANTLRv4Parser.ParserRuleSpecContext):                    
                    if actions:
                        rule.args = parse_arg_action_block(node, 'args')
                        rule.locals = parse_arg_action_block(node.localsSpec(), 'locals')
                        rule.returns = parse_arg_action_block(node.ruleReturns(), 'returns')

                        for prequel in node.rulePrequel() or []:
                            rule_action = prequel.ruleAction()
                            if rule_action:
                                action_name = str(rule_action.identifier().TOKEN_REF() or rule_action.identifier().RULE_REF())
                                if action_name not in ['init', 'after']:
                                    continue

                                src = ''.join(str(child) for child in rule_action.actionBlock().ACTION_CONTENT()).strip()
                                if action_name == 'init':
                                    rule.init = src
                                elif action_name == 'after':
                                    rule.after = src
                    build_expr(node.ruleBlock(), parent_id)

                elif isinstance(node, (ANTLRv4Parser.RuleAltListContext, ANTLRv4Parser.AltListContext, ANTLRv4Parser.LexerAltListContext)):
                    children = [child for child in node.children if isinstance(child, ParserRuleContext)]
                    if len(children) == 1:
                        build_expr(children[0], parent_id)
                        return

                    conditions = [find_conditions(child) for child in children]
                    labels = [str(child.identifier().TOKEN_REF() or child.identifier().RULE_REF()) for child in children if child.identifier()] if isinstance(node, ANTLRv4Parser.RuleAltListContext) else []
                    labels = [label[0].upper() + label[1:] for label in labels]
                    recurring_labels = {name for name, cnt in Counter(labels).items() if cnt > 1}
                    assert len(labels) == 0 or len(labels) == len(children)
                    alt_id = graph.add_node(AlternationNode(idx=alt_idx[rule.name], conditions=append_unique(graph.alt_conds, conditions) if all(isfloat(cond) for cond in conditions) else conditions, rule_id=rule.id))
                    alt_idx[rule.name] += 1
                    graph.add_edge(frm=parent_id, to=alt_id)
                    for i, child in enumerate(children):
                        alternative_id = graph.add_node(AlternativeNode(rule_id=rule.id, alt_idx=graph.vertices[alt_id].idx, idx=i))
                        graph.add_edge(frm=alt_id, to=alternative_id)

                        if labels:
                            label_idx = labels[:i + 1].count(labels[i]) - 1 if labels[i] in recurring_labels else None
                            rule_node_id = graph.add_node(UnparserRuleNode(name=(rule.name, labels[i], label_idx) if label_idx is not None else (rule.name, labels[i])))
                            graph.add_edge(frm=alternative_id, to=rule_node_id)
                            build_rule(graph.vertices[rule_node_id], child)
                        else:
                            build_expr(child, alternative_id)


                    for label in recurring_labels:
                        new_conditions = [cond if labels[ci] == label else '0' for ci, cond in enumerate(conditions)]
                        recurring_rule_id = graph.add_node(UnparserRuleNode(name=(rule.name, label), trampoline=True))
                        labeled_alt_id = graph.add_node(AlternationNode(idx=0,
                                                                        conditions=append_unique(graph.alt_conds, new_conditions) if all(isfloat(cond) for cond in new_conditions) else new_conditions,
                                                                        rule_id=recurring_rule_id))
                        graph.add_edge(frm=recurring_rule_id, to=labeled_alt_id)
                        recurring_idx = 0
                        for i in range(len(children)):
                            labeled_alternative_id = graph.add_node(AlternativeNode(rule_id=recurring_rule_id, alt_idx=0, idx=i))
                            graph.add_edge(frm=labeled_alt_id, to=labeled_alternative_id)
                            if labels[i] == label:
                                graph.add_edge(frm=labeled_alternative_id, to=(rule.name, label, recurring_idx))
                                recurring_idx += 1
                            else:
                                graph.add_edge(frm=labeled_alternative_id, to=lambda_id)

                elif isinstance(node, (ANTLRv4Parser.AlternativeContext, ANTLRv4Parser.LexerAltContext)):
                    children = node.element() if isinstance(node, ANTLRv4Parser.AlternativeContext) else node.lexerElements().lexerElement()
                    for child in children:
                        build_expr(child, parent_id)

                    if not graph.vertices[parent_id].out_neighbours:
                        graph.add_edge(frm=parent_id, to=lambda_id)

                elif isinstance(node, (ANTLRv4Parser.ElementContext, ANTLRv4Parser.LexerElementContext)):
                    if node.actionBlock():
                        if not actions or node.QUESTION():
                            return

                        graph.add_edge(frm=parent_id, to=graph.add_node(ActionNode(src=''.join(str(child) for child in node.actionBlock().ACTION_CONTENT()))))
                        return

                    suffix = None
                    if node.ebnfSuffix():
                        suffix = node.ebnfSuffix()
                    elif hasattr(node, 'ebnf') and node.ebnf() and node.ebnf().blockSuffix():
                        suffix = node.ebnf().blockSuffix().ebnfSuffix()

                    if not suffix:
                        build_expr(node.children[0], parent_id)
                        return

                    suffix = str(suffix.children[0])
                    quant_ranges = {'?': {'start': 0, 'stop': 1}, '*': {'start': 0, 'stop': 'inf'}, '+': {'start': 1, 'stop': 'inf'}}
                    quant_id = graph.add_node(QuantifierNode(rule_id=rule.id, idx=quant_idx[rule.name], **quant_ranges[suffix]))
                    quant_idx[rule.name] += 1
                    graph.add_edge(frm=parent_id, to=quant_id)
                    build_expr(node.children[0], quant_id)

                elif isinstance(node, ANTLRv4Parser.LabeledElementContext):
                    build_expr(node.atom() or node.block(), parent_id)
                    # Do not save variables if actions are not allowed.
                    if not actions:
                        return

                    ident = node.identifier()
                    name = str(ident.RULE_REF() or ident.TOKEN_REF())
                    is_list = node.PLUS_ASSIGN() is not None
                    graph.add_edge(frm=parent_id, to=graph.add_node(VariableNode(name=name, is_list=is_list)))
                    rule.labels[name] = is_list

                elif isinstance(node, ANTLRv4Parser.RulerefContext):
                    graph.add_edge(frm=parent_id, to=str(node.RULE_REF()), args=parse_arg_action_block(node, 'call') if actions else None)

                elif isinstance(node, (ANTLRv4Parser.LexerAtomContext, ANTLRv4Parser.AtomContext)):
                    def get_rule_text(node):
                        current = node
                        while current:
                            if isinstance(current, ANTLRv4Parser.ParserRuleSpecContext):
                                rule_name = str(current.RULE_REF())
                                if current.ruleBlock():
                                    rule_body = current.ruleBlock().getText()
                                    return (rule_name, rule_body)
                                return rule_name
                            elif isinstance(current, ANTLRv4Parser.LexerRuleSpecContext):
                                rule_name = str(current.TOKEN_REF())
                                if current.lexerRuleBlock():
                                    rule_body = current.lexerRuleBlock().getText()
                                    return (rule_name, rule_body)
                                return rule_name
                            current = current.parentCtx
                        return None                    
                    
                    if re_lexical_rules:
                        rule_name, rule_body = get_rule_text(node)

                        if rule_name and rule_name not in graph.lexicals and rule_name in re_lexical_rules:
                            if re_lexical_rules_special_token and len(re_lexical_rules_special_token) == 2:
                                rule_body = re_lexical_rules_special_token[0]+rule_body+re_lexical_rules_special_token[1]
                            graph.lexicals[rule_name] = rule_body


                    if node.DOT():
                        if isinstance(node, ANTLRv4Parser.LexerAtomContext):                            

                            graph.add_edge(frm=parent_id, to=graph.add_node(CharsetNode(rule_id=rule.id, idx=chr_idx[rule.name], charset=dot_charset)))
                            chr_idx[rule.name] += 1
                        else:
                            if '_dot' not in graph.vertices:
                                parser_dot_id = graph.add_node(UnparserRuleNode(name='_dot'))
                                unlexer_ids = [v.name for vid, v in graph.vertices.items() if isinstance(v, UnlexerRuleNode)]
                                alt_id = graph.add_node(AlternationNode(rule_id=parser_dot_id, idx=0, conditions=[1] * len(unlexer_ids)))
                                graph.add_edge(frm=parser_dot_id, to=alt_id)
                                for i, lexer_id in enumerate(unlexer_ids):
                                    alternative_id = graph.add_node(AlternativeNode(rule_id=parser_dot_id, alt_idx=0, idx=i))
                                    graph.add_edge(frm=alt_id, to=alternative_id)
                                    graph.add_edge(frm=alternative_id, to=lexer_id)
                            graph.add_edge(frm=parent_id, to='_dot')

                    elif node.notSet():
                        if node.notSet().setElement():
                            not_ranges = chars_from_set(node.notSet().setElement())
                        else:
                            not_ranges = []
                            for set_element in node.notSet().blockSet().setElement():
                                not_ranges.extend(chars_from_set(set_element))

                        charset = unique_charset(multirange_diff(graph.charsets[dot_charset], sorted(not_ranges, key=lambda x: x[0])))
                        graph.add_edge(frm=parent_id, to=graph.add_node(CharsetNode(rule_id=rule.id, idx=chr_idx[rule.name], charset=charset)))
                        chr_idx[rule.name] += 1

                    elif isinstance(node, ANTLRv4Parser.LexerAtomContext) and node.characterRange():
                        start, end = character_range_interval(node)
                        if lexer_rule:
                            rule.start_ranges.append((start, end))

                        charset = unique_charset([(start, end)])
                        graph.add_edge(frm=parent_id, to=graph.add_node(CharsetNode(rule_id=rule.id, idx=chr_idx[rule.name], charset=charset)))
                        chr_idx[rule.name] += 1

                    elif isinstance(node, ANTLRv4Parser.LexerAtomContext) and node.LEXER_CHAR_SET():
                        ranges = lexer_charset_interval(str(node.LEXER_CHAR_SET())[1:-1])
                        if lexer_rule:
                            rule.start_ranges.extend(ranges)

                        charset = unique_charset(sorted(ranges, key=lambda x: x[0]))
                        graph.add_edge(frm=parent_id, to=graph.add_node(CharsetNode(rule_id=rule.id, idx=chr_idx[rule.name], charset=charset)))
                        chr_idx[rule.name] += 1

                    for child in node.children:
                        build_expr(child, parent_id)

                elif isinstance(node, ANTLRv4Parser.TerminalContext):
                    if node.TOKEN_REF():
                        if str(node.TOKEN_REF()) != 'EOF':
                            graph.add_edge(frm=parent_id, to=str(node.TOKEN_REF()))

                    elif node.STRING_LITERAL():
                        src = unescape_string(str(node.STRING_LITERAL())[1:-1])

                        if lexer_rule:
                            rule.start_ranges.append((ord(src[0]), ord(src[0]) + 1))
                            graph.add_edge(frm=parent_id, to=graph.add_node(LiteralNode(src=src)))
                        else:
                            lit_id = literal_lookup.get(src)
                            if not lit_id:
                                lit_id = graph.add_node(UnlexerRuleNode())
                                literal_lookup[src] = lit_id
                                graph.add_edge(frm=lit_id, to=graph.add_node(LiteralNode(src=src)))
                            graph.add_edge(frm=parent_id, to=lit_id)

                elif isinstance(node, ParserRuleContext) and node.getChildCount():
                    for child in node.children:
                        build_expr(child, parent_id)

            if lexer_rule:
                rule.start_ranges = []

            build_expr(node, rule.id)

            if lexer_rule and len(rule.out_edges) == 1 and isinstance(rule.out_edges[0].dst, LiteralNode):
                literal_lookup[rule.out_edges[0].dst.src] = rule.id

        def build_prequel(node):
            assert isinstance(node, ANTLRv4Parser.GrammarSpecContext)

            if not graph.name:
                graph.name = re.sub(r'^(.+?)(Lexer|Parser)?$', r'\1Generator', str(node.grammarDecl().identifier().TOKEN_REF() or node.grammarDecl().identifier().RULE_REF()))

            for prequelConstruct in node.prequelConstruct() if node.prequelConstruct() else ():
                for option in prequelConstruct.optionsSpec().option() if prequelConstruct.optionsSpec() else ():
                    ident = option.identifier()
                    ident = str(ident.RULE_REF() or ident.TOKEN_REF())
                    graph.options[ident] = option.optionValue().getText()

                for identifier in prequelConstruct.tokensSpec().idList().identifier() if prequelConstruct.tokensSpec() and prequelConstruct.tokensSpec().idList() else ():
                    assert identifier.TOKEN_REF() is not None, 'Token names must start with uppercase letter.'
                    graph.add_node(ImagRuleNode(id=str(identifier.TOKEN_REF())))

                if prequelConstruct.action_() and actions:
                    action = prequelConstruct.action_()
                    action_ident = action.identifier()
                    action_type = str(action_ident.RULE_REF() or action_ident.TOKEN_REF())
                    raw_action_src = ''.join(str(child) for child in action.actionBlock().ACTION_CONTENT())

                    if action_type == 'members':
                        graph.members += raw_action_src
                    elif action_type == 'header':
                        graph.header += raw_action_src

        def build_rules(node):
            generator_rules, duplicate_rules = [], []
            for rule in node.rules().ruleSpec():
                if rule.parserRuleSpec():
                    """
                    rule_spec.RULE_REF():
                    query
                    primary
                    binaryExpression
                    searchCondition
                    dateSearch
                    binaryDateSearch
                    dateSearchinfo
                    relativelydate
                    absolutedate
                    pathSearch
                    nameSearch
                    sizeSearch
                    typeSearch
                    durationSearch
                    metaSearch
                    quantityCondition
                    contentSearch
                    comparison_type
                    string
                    filename
                    """
                    rule_spec = rule.parserRuleSpec()
                    rule_node = UnparserRuleNode(name=str(rule_spec.RULE_REF()))
                    antlr_node = rule_spec
                elif rule.lexerRuleSpec():
                    rule_spec = rule.lexerRuleSpec()
                    """
                    SPACE
                    STRING_VALUE
                    NUMBER_VALUE
                    """
                    rule_node = UnlexerRuleNode(name=str(rule_spec.TOKEN_REF()))
                    antlr_node = rule_spec.lexerRuleBlock()
                else:
                    assert False, 'Should not get here.'

                if rule_node.id not in graph.vertices:
                    graph.add_node(rule_node)
                    generator_rules.append((rule_node, antlr_node))
                else:
                    duplicate_rules.append(rule_node.id)

            for mode_spec in node.modeSpec():
                for rule_spec in mode_spec.lexerRuleSpec():
                    
                    rule_node = UnlexerRuleNode(name=str(rule_spec.TOKEN_REF()))
                    if rule_node.id not in graph.vertices:
                        graph.add_node(rule_node)
                        generator_rules.append((rule_node, rule_spec.lexerRuleBlock()))
                    else:
                        duplicate_rules.append(rule_node.id)

            if duplicate_rules:
                raise ValueError(f'Rule redefinition(s): {", ".join(["_".join(id) for id in duplicate_rules])}')

            for rule_args in sorted(generator_rules, key=lambda r: int(isinstance(r[0], UnparserRuleNode))):
                build_rule(*rule_args)

            if default_rule:
                graph.default_rule = default_rule
            elif node.grammarDecl().grammarType().PARSER() or not (node.grammarDecl().grammarType().LEXER() or node.grammarDecl().grammarType().PARSER()):
                graph.default_rule = generator_rules[0][0].name

        graph = CFGGrammarGraph()
        lambda_id = graph.add_node(LambdaNode())

        for root in [lexer_root, parser_root]:
            if root:
                build_prequel(root)
        graph.options.update(options or {})

        dot_charset = unique_charset(dot_ranges[graph.dot])

        literal_lookup = {}
        alt_idx, quant_idx, chr_idx = Counter(), Counter(), Counter()

        for root in [lexer_root, parser_root]:
            if root:
                build_rules(root)

        graph.calc_min_sizes()
        graph.find_immutable_rules()
        return graph