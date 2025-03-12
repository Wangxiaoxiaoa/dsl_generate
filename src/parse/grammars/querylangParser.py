# Generated from /root/autodl-tmp/xiao/CFG_generate/grammars_samples/querylang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,203,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,55,8,1,
        10,1,12,1,58,9,1,1,2,1,2,1,2,1,2,1,2,3,2,65,8,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,3,3,76,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,5,4,87,8,4,10,4,12,4,90,9,4,1,5,1,5,1,5,1,5,1,5,3,5,97,8,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,111,8,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,
        10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,3,11,147,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,193,
        8,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,20,0,0,21,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,2,2,0,20,20,
        24,28,2,0,16,16,29,29,198,0,42,1,0,0,0,2,45,1,0,0,0,4,64,1,0,0,0,
        6,75,1,0,0,0,8,77,1,0,0,0,10,96,1,0,0,0,12,110,1,0,0,0,14,112,1,
        0,0,0,16,118,1,0,0,0,18,120,1,0,0,0,20,126,1,0,0,0,22,146,1,0,0,
        0,24,148,1,0,0,0,26,154,1,0,0,0,28,160,1,0,0,0,30,174,1,0,0,0,32,
        192,1,0,0,0,34,194,1,0,0,0,36,196,1,0,0,0,38,198,1,0,0,0,40,200,
        1,0,0,0,42,43,3,2,1,0,43,44,5,0,0,1,44,1,1,0,0,0,45,56,3,4,2,0,46,
        47,5,30,0,0,47,48,5,1,0,0,48,49,5,30,0,0,49,55,3,4,2,0,50,51,5,30,
        0,0,51,52,5,2,0,0,52,53,5,30,0,0,53,55,3,4,2,0,54,46,1,0,0,0,54,
        50,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,3,1,0,0,
        0,58,56,1,0,0,0,59,60,5,3,0,0,60,61,3,2,1,0,61,62,5,4,0,0,62,65,
        1,0,0,0,63,65,3,6,3,0,64,59,1,0,0,0,64,63,1,0,0,0,65,5,1,0,0,0,66,
        76,3,8,4,0,67,76,3,18,9,0,68,76,3,20,10,0,69,76,3,22,11,0,70,76,
        3,24,12,0,71,76,3,26,13,0,72,76,3,28,14,0,73,76,3,30,15,0,74,76,
        3,32,16,0,75,66,1,0,0,0,75,67,1,0,0,0,75,68,1,0,0,0,75,69,1,0,0,
        0,75,70,1,0,0,0,75,71,1,0,0,0,75,72,1,0,0,0,75,73,1,0,0,0,75,74,
        1,0,0,0,76,7,1,0,0,0,77,88,3,10,5,0,78,79,5,30,0,0,79,80,5,1,0,0,
        80,81,5,30,0,0,81,87,3,10,5,0,82,83,5,30,0,0,83,84,5,2,0,0,84,85,
        5,30,0,0,85,87,3,10,5,0,86,78,1,0,0,0,86,82,1,0,0,0,87,90,1,0,0,
        0,88,86,1,0,0,0,88,89,1,0,0,0,89,9,1,0,0,0,90,88,1,0,0,0,91,92,5,
        3,0,0,92,93,3,12,6,0,93,94,5,4,0,0,94,97,1,0,0,0,95,97,3,12,6,0,
        96,91,1,0,0,0,96,95,1,0,0,0,97,11,1,0,0,0,98,99,5,5,0,0,99,100,5,
        30,0,0,100,101,3,34,17,0,101,102,5,30,0,0,102,103,3,16,8,0,103,111,
        1,0,0,0,104,105,5,5,0,0,105,106,5,30,0,0,106,107,3,34,17,0,107,108,
        5,30,0,0,108,109,3,14,7,0,109,111,1,0,0,0,110,98,1,0,0,0,110,104,
        1,0,0,0,111,13,1,0,0,0,112,113,5,6,0,0,113,114,5,30,0,0,114,115,
        5,7,0,0,115,116,5,30,0,0,116,117,3,36,18,0,117,15,1,0,0,0,118,119,
        5,31,0,0,119,17,1,0,0,0,120,121,5,8,0,0,121,122,5,30,0,0,122,123,
        3,40,20,0,123,124,5,30,0,0,124,125,3,36,18,0,125,19,1,0,0,0,126,
        127,5,9,0,0,127,128,5,30,0,0,128,129,5,10,0,0,129,130,5,30,0,0,130,
        131,3,36,18,0,131,21,1,0,0,0,132,133,5,11,0,0,133,134,5,30,0,0,134,
        135,3,34,17,0,135,136,5,30,0,0,136,137,3,36,18,0,137,147,1,0,0,0,
        138,139,5,11,0,0,139,140,5,30,0,0,140,141,3,34,17,0,141,142,5,30,
        0,0,142,143,5,12,0,0,143,144,5,30,0,0,144,145,3,38,19,0,145,147,
        1,0,0,0,146,132,1,0,0,0,146,138,1,0,0,0,147,23,1,0,0,0,148,149,5,
        13,0,0,149,150,5,30,0,0,150,151,3,40,20,0,151,152,5,30,0,0,152,153,
        3,36,18,0,153,25,1,0,0,0,154,155,5,14,0,0,155,156,5,30,0,0,156,157,
        3,34,17,0,157,158,5,30,0,0,158,159,3,36,18,0,159,27,1,0,0,0,160,
        161,5,15,0,0,161,162,5,30,0,0,162,163,5,16,0,0,163,164,5,30,0,0,
        164,165,3,36,18,0,165,166,5,30,0,0,166,167,5,17,0,0,167,168,5,30,
        0,0,168,169,5,18,0,0,169,170,5,30,0,0,170,171,3,40,20,0,171,172,
        5,30,0,0,172,173,3,36,18,0,173,29,1,0,0,0,174,175,5,19,0,0,175,176,
        5,30,0,0,176,177,5,20,0,0,177,178,5,30,0,0,178,179,5,32,0,0,179,
        31,1,0,0,0,180,181,5,21,0,0,181,182,5,30,0,0,182,183,5,10,0,0,183,
        184,5,30,0,0,184,193,3,36,18,0,185,186,5,21,0,0,186,187,5,30,0,0,
        187,188,5,22,0,0,188,189,5,30,0,0,189,190,5,23,0,0,190,191,5,30,
        0,0,191,193,3,38,19,0,192,180,1,0,0,0,192,185,1,0,0,0,193,33,1,0,
        0,0,194,195,7,0,0,0,195,35,1,0,0,0,196,197,5,31,0,0,197,37,1,0,0,
        0,198,199,5,31,0,0,199,39,1,0,0,0,200,201,7,1,0,0,201,41,1,0,0,0,
        10,54,56,64,75,86,88,96,110,146,192
    ]

class querylangParser ( Parser ):

    grammarFileName = "querylang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'AND'", "'OR'", "'('", "')'", "'DATE'", 
                     "'CURRENT'", "'-'", "'PATH'", "'NAME'", "'CONTAINS'", 
                     "'SIZE'", "'FILE_SIZE'", "'TYPE'", "'DURATION'", "'META_TYPE'", 
                     "'IS'", "'WITH'", "'META_VALUE'", "'QUANTITY'", "'='", 
                     "'CONTENT'", "'EQUALS'", "'FILE'", "'<'", "'>'", "'!='", 
                     "'<='", "'>='", "'IS NOT'", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SPACE", "STRING", "NUMBER_VALUE" ]

    RULE_query = 0
    RULE_primary = 1
    RULE_binaryExpression = 2
    RULE_searchCondition = 3
    RULE_dateSearch = 4
    RULE_binaryDateSearch = 5
    RULE_dateSearchinfo = 6
    RULE_relativelydate = 7
    RULE_absolutedate = 8
    RULE_pathSearch = 9
    RULE_nameSearch = 10
    RULE_sizeSearch = 11
    RULE_typeSearch = 12
    RULE_durationSearch = 13
    RULE_metaSearch = 14
    RULE_quantityCondition = 15
    RULE_contentSearch = 16
    RULE_comparison_type = 17
    RULE_string = 18
    RULE_filename = 19
    RULE_is_or_not = 20

    ruleNames =  [ "query", "primary", "binaryExpression", "searchCondition", 
                   "dateSearch", "binaryDateSearch", "dateSearchinfo", "relativelydate", 
                   "absolutedate", "pathSearch", "nameSearch", "sizeSearch", 
                   "typeSearch", "durationSearch", "metaSearch", "quantityCondition", 
                   "contentSearch", "comparison_type", "string", "filename", 
                   "is_or_not" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    SPACE=30
    STRING=31
    NUMBER_VALUE=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(querylangParser.PrimaryContext,0)


        def EOF(self):
            return self.getToken(querylangParser.EOF, 0)

        def getRuleIndex(self):
            return querylangParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = querylangParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.primary()
            self.state = 43
            self.match(querylangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def binaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(querylangParser.BinaryExpressionContext)
            else:
                return self.getTypedRuleContext(querylangParser.BinaryExpressionContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(querylangParser.SPACE)
            else:
                return self.getToken(querylangParser.SPACE, i)

        def getRuleIndex(self):
            return querylangParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = querylangParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.binaryExpression()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 54
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 46
                    self.match(querylangParser.SPACE)
                    self.state = 47
                    self.match(querylangParser.T__0)
                    self.state = 48
                    self.match(querylangParser.SPACE)
                    self.state = 49
                    self.binaryExpression()
                    pass

                elif la_ == 2:
                    self.state = 50
                    self.match(querylangParser.SPACE)
                    self.state = 51
                    self.match(querylangParser.T__1)
                    self.state = 52
                    self.match(querylangParser.SPACE)
                    self.state = 53
                    self.binaryExpression()
                    pass


                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(querylangParser.PrimaryContext,0)


        def searchCondition(self):
            return self.getTypedRuleContext(querylangParser.SearchConditionContext,0)


        def getRuleIndex(self):
            return querylangParser.RULE_binaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryExpression" ):
                listener.enterBinaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryExpression" ):
                listener.exitBinaryExpression(self)




    def binaryExpression(self):

        localctx = querylangParser.BinaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_binaryExpression)
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(querylangParser.T__2)
                self.state = 60
                self.primary()
                self.state = 61
                self.match(querylangParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.searchCondition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SearchConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dateSearch(self):
            return self.getTypedRuleContext(querylangParser.DateSearchContext,0)


        def pathSearch(self):
            return self.getTypedRuleContext(querylangParser.PathSearchContext,0)


        def nameSearch(self):
            return self.getTypedRuleContext(querylangParser.NameSearchContext,0)


        def sizeSearch(self):
            return self.getTypedRuleContext(querylangParser.SizeSearchContext,0)


        def typeSearch(self):
            return self.getTypedRuleContext(querylangParser.TypeSearchContext,0)


        def durationSearch(self):
            return self.getTypedRuleContext(querylangParser.DurationSearchContext,0)


        def metaSearch(self):
            return self.getTypedRuleContext(querylangParser.MetaSearchContext,0)


        def quantityCondition(self):
            return self.getTypedRuleContext(querylangParser.QuantityConditionContext,0)


        def contentSearch(self):
            return self.getTypedRuleContext(querylangParser.ContentSearchContext,0)


        def getRuleIndex(self):
            return querylangParser.RULE_searchCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSearchCondition" ):
                listener.enterSearchCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSearchCondition" ):
                listener.exitSearchCondition(self)




    def searchCondition(self):

        localctx = querylangParser.SearchConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_searchCondition)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.dateSearch()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.pathSearch()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.nameSearch()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.sizeSearch()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.typeSearch()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.durationSearch()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.metaSearch()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 8)
                self.state = 73
                self.quantityCondition()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 9)
                self.state = 74
                self.contentSearch()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateSearchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def binaryDateSearch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(querylangParser.BinaryDateSearchContext)
            else:
                return self.getTypedRuleContext(querylangParser.BinaryDateSearchContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(querylangParser.SPACE)
            else:
                return self.getToken(querylangParser.SPACE, i)

        def getRuleIndex(self):
            return querylangParser.RULE_dateSearch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDateSearch" ):
                listener.enterDateSearch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDateSearch" ):
                listener.exitDateSearch(self)




    def dateSearch(self):

        localctx = querylangParser.DateSearchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dateSearch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.binaryDateSearch()
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 86
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        self.state = 78
                        self.match(querylangParser.SPACE)
                        self.state = 79
                        self.match(querylangParser.T__0)
                        self.state = 80
                        self.match(querylangParser.SPACE)
                        self.state = 81
                        self.binaryDateSearch()
                        pass

                    elif la_ == 2:
                        self.state = 82
                        self.match(querylangParser.SPACE)
                        self.state = 83
                        self.match(querylangParser.T__1)
                        self.state = 84
                        self.match(querylangParser.SPACE)
                        self.state = 85
                        self.binaryDateSearch()
                        pass

             
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryDateSearchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dateSearchinfo(self):
            return self.getTypedRuleContext(querylangParser.DateSearchinfoContext,0)


        def getRuleIndex(self):
            return querylangParser.RULE_binaryDateSearch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryDateSearch" ):
                listener.enterBinaryDateSearch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryDateSearch" ):
                listener.exitBinaryDateSearch(self)




    def binaryDateSearch(self):

        localctx = querylangParser.BinaryDateSearchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_binaryDateSearch)
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.match(querylangParser.T__2)
                self.state = 92
                self.dateSearchinfo()
                self.state = 93
                self.match(querylangParser.T__3)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.dateSearchinfo()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateSearchinfoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(querylangParser.SPACE)
            else:
                return self.getToken(querylangParser.SPACE, i)

        def comparison_type(self):
            return self.getTypedRuleContext(querylangParser.Comparison_typeContext,0)


        def absolutedate(self):
            return self.getTypedRuleContext(querylangParser.AbsolutedateContext,0)


        def relativelydate(self):
            return self.getTypedRuleContext(querylangParser.RelativelydateContext,0)


        def getRuleIndex(self):
            return querylangParser.RULE_dateSearchinfo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDateSearchinfo" ):
                listener.enterDateSearchinfo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDateSearchinfo" ):
                listener.exitDateSearchinfo(self)




    def dateSearchinfo(self):

        localctx = querylangParser.DateSearchinfoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dateSearchinfo)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(querylangParser.T__4)
                self.state = 99
                self.match(querylangParser.SPACE)
                self.state = 100
                self.comparison_type()
                self.state = 101
                self.match(querylangParser.SPACE)
                self.state = 102
                self.absolutedate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(querylangParser.T__4)
                self.state = 105
                self.match(querylangParser.SPACE)
                self.state = 106
                self.comparison_type()
                self.state = 107
                self.match(querylangParser.SPACE)
                self.state = 108
                self.relativelydate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelativelydateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(querylangParser.SPACE)
            else:
                return self.getToken(querylangParser.SPACE, i)

        def string(self):
            return self.getTypedRuleContext(querylangParser.StringContext,0)


        def getRuleIndex(self):
            return querylangParser.RULE_relativelydate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelativelydate" ):
                listener.enterRelativelydate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelativelydate" ):
                listener.exitRelativelydate(self)




    def relativelydate(self):

        localctx = querylangParser.RelativelydateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_relativelydate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(querylangParser.T__5)
            self.state = 113
            self.match(querylangParser.SPACE)
            self.state = 114
            self.match(querylangParser.T__6)
            self.state = 115
            self.match(querylangParser.SPACE)
            self.state = 116
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AbsolutedateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(querylangParser.STRING, 0)

        def getRuleIndex(self):
            return querylangParser.RULE_absolutedate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbsolutedate" ):
                listener.enterAbsolutedate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbsolutedate" ):
                listener.exitAbsolutedate(self)




    def absolutedate(self):

        localctx = querylangParser.AbsolutedateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_absolutedate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(querylangParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathSearchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(querylangParser.SPACE)
            else:
                return self.getToken(querylangParser.SPACE, i)

        def is_or_not(self):
            return self.getTypedRuleContext(querylangParser.Is_or_notContext,0)


        def string(self):
            return self.getTypedRuleContext(querylangParser.StringContext,0)


        def getRuleIndex(self):
            return querylangParser.RULE_pathSearch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathSearch" ):
                listener.enterPathSearch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathSearch" ):
                listener.exitPathSearch(self)




    def pathSearch(self):

        localctx = querylangParser.PathSearchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pathSearch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(querylangParser.T__7)
            self.state = 121
            self.match(querylangParser.SPACE)
            self.state = 122
            self.is_or_not()
            self.state = 123
            self.match(querylangParser.SPACE)
            self.state = 124
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameSearchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(querylangParser.SPACE)
            else:
                return self.getToken(querylangParser.SPACE, i)

        def string(self):
            return self.getTypedRuleContext(querylangParser.StringContext,0)


        def getRuleIndex(self):
            return querylangParser.RULE_nameSearch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameSearch" ):
                listener.enterNameSearch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameSearch" ):
                listener.exitNameSearch(self)




    def nameSearch(self):

        localctx = querylangParser.NameSearchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_nameSearch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(querylangParser.T__8)
            self.state = 127
            self.match(querylangParser.SPACE)
            self.state = 128
            self.match(querylangParser.T__9)
            self.state = 129
            self.match(querylangParser.SPACE)
            self.state = 130
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeSearchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(querylangParser.SPACE)
            else:
                return self.getToken(querylangParser.SPACE, i)

        def comparison_type(self):
            return self.getTypedRuleContext(querylangParser.Comparison_typeContext,0)


        def string(self):
            return self.getTypedRuleContext(querylangParser.StringContext,0)


        def filename(self):
            return self.getTypedRuleContext(querylangParser.FilenameContext,0)


        def getRuleIndex(self):
            return querylangParser.RULE_sizeSearch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeSearch" ):
                listener.enterSizeSearch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeSearch" ):
                listener.exitSizeSearch(self)




    def sizeSearch(self):

        localctx = querylangParser.SizeSearchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sizeSearch)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(querylangParser.T__10)
                self.state = 133
                self.match(querylangParser.SPACE)
                self.state = 134
                self.comparison_type()
                self.state = 135
                self.match(querylangParser.SPACE)
                self.state = 136
                self.string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(querylangParser.T__10)
                self.state = 139
                self.match(querylangParser.SPACE)
                self.state = 140
                self.comparison_type()
                self.state = 141
                self.match(querylangParser.SPACE)
                self.state = 142
                self.match(querylangParser.T__11)
                self.state = 143
                self.match(querylangParser.SPACE)
                self.state = 144
                self.filename()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSearchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(querylangParser.SPACE)
            else:
                return self.getToken(querylangParser.SPACE, i)

        def is_or_not(self):
            return self.getTypedRuleContext(querylangParser.Is_or_notContext,0)


        def string(self):
            return self.getTypedRuleContext(querylangParser.StringContext,0)


        def getRuleIndex(self):
            return querylangParser.RULE_typeSearch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSearch" ):
                listener.enterTypeSearch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSearch" ):
                listener.exitTypeSearch(self)




    def typeSearch(self):

        localctx = querylangParser.TypeSearchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_typeSearch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(querylangParser.T__12)
            self.state = 149
            self.match(querylangParser.SPACE)
            self.state = 150
            self.is_or_not()
            self.state = 151
            self.match(querylangParser.SPACE)
            self.state = 152
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DurationSearchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(querylangParser.SPACE)
            else:
                return self.getToken(querylangParser.SPACE, i)

        def comparison_type(self):
            return self.getTypedRuleContext(querylangParser.Comparison_typeContext,0)


        def string(self):
            return self.getTypedRuleContext(querylangParser.StringContext,0)


        def getRuleIndex(self):
            return querylangParser.RULE_durationSearch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDurationSearch" ):
                listener.enterDurationSearch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDurationSearch" ):
                listener.exitDurationSearch(self)




    def durationSearch(self):

        localctx = querylangParser.DurationSearchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_durationSearch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(querylangParser.T__13)
            self.state = 155
            self.match(querylangParser.SPACE)
            self.state = 156
            self.comparison_type()
            self.state = 157
            self.match(querylangParser.SPACE)
            self.state = 158
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetaSearchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(querylangParser.SPACE)
            else:
                return self.getToken(querylangParser.SPACE, i)

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(querylangParser.StringContext)
            else:
                return self.getTypedRuleContext(querylangParser.StringContext,i)


        def is_or_not(self):
            return self.getTypedRuleContext(querylangParser.Is_or_notContext,0)


        def getRuleIndex(self):
            return querylangParser.RULE_metaSearch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetaSearch" ):
                listener.enterMetaSearch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetaSearch" ):
                listener.exitMetaSearch(self)




    def metaSearch(self):

        localctx = querylangParser.MetaSearchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_metaSearch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(querylangParser.T__14)
            self.state = 161
            self.match(querylangParser.SPACE)
            self.state = 162
            self.match(querylangParser.T__15)
            self.state = 163
            self.match(querylangParser.SPACE)
            self.state = 164
            self.string()
            self.state = 165
            self.match(querylangParser.SPACE)
            self.state = 166
            self.match(querylangParser.T__16)
            self.state = 167
            self.match(querylangParser.SPACE)
            self.state = 168
            self.match(querylangParser.T__17)
            self.state = 169
            self.match(querylangParser.SPACE)
            self.state = 170
            self.is_or_not()
            self.state = 171
            self.match(querylangParser.SPACE)
            self.state = 172
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantityConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(querylangParser.SPACE)
            else:
                return self.getToken(querylangParser.SPACE, i)

        def NUMBER_VALUE(self):
            return self.getToken(querylangParser.NUMBER_VALUE, 0)

        def getRuleIndex(self):
            return querylangParser.RULE_quantityCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantityCondition" ):
                listener.enterQuantityCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantityCondition" ):
                listener.exitQuantityCondition(self)




    def quantityCondition(self):

        localctx = querylangParser.QuantityConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_quantityCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(querylangParser.T__18)
            self.state = 175
            self.match(querylangParser.SPACE)
            self.state = 176
            self.match(querylangParser.T__19)
            self.state = 177
            self.match(querylangParser.SPACE)
            self.state = 178
            self.match(querylangParser.NUMBER_VALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentSearchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(querylangParser.SPACE)
            else:
                return self.getToken(querylangParser.SPACE, i)

        def string(self):
            return self.getTypedRuleContext(querylangParser.StringContext,0)


        def filename(self):
            return self.getTypedRuleContext(querylangParser.FilenameContext,0)


        def getRuleIndex(self):
            return querylangParser.RULE_contentSearch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContentSearch" ):
                listener.enterContentSearch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContentSearch" ):
                listener.exitContentSearch(self)




    def contentSearch(self):

        localctx = querylangParser.ContentSearchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_contentSearch)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(querylangParser.T__20)
                self.state = 181
                self.match(querylangParser.SPACE)
                self.state = 182
                self.match(querylangParser.T__9)
                self.state = 183
                self.match(querylangParser.SPACE)
                self.state = 184
                self.string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(querylangParser.T__20)
                self.state = 186
                self.match(querylangParser.SPACE)
                self.state = 187
                self.match(querylangParser.T__21)
                self.state = 188
                self.match(querylangParser.SPACE)
                self.state = 189
                self.match(querylangParser.T__22)
                self.state = 190
                self.match(querylangParser.SPACE)
                self.state = 191
                self.filename()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return querylangParser.RULE_comparison_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_type" ):
                listener.enterComparison_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_type" ):
                listener.exitComparison_type(self)




    def comparison_type(self):

        localctx = querylangParser.Comparison_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comparison_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 521142272) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(querylangParser.STRING, 0)

        def getRuleIndex(self):
            return querylangParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = querylangParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(querylangParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilenameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(querylangParser.STRING, 0)

        def getRuleIndex(self):
            return querylangParser.RULE_filename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilename" ):
                listener.enterFilename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilename" ):
                listener.exitFilename(self)




    def filename(self):

        localctx = querylangParser.FilenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_filename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(querylangParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Is_or_notContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return querylangParser.RULE_is_or_not

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIs_or_not" ):
                listener.enterIs_or_not(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIs_or_not" ):
                listener.exitIs_or_not(self)




    def is_or_not(self):

        localctx = querylangParser.Is_or_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_is_or_not)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not(_la==16 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





