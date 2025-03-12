# Generated from /root/autodl-tmp/xiao/CFG_generate/grammars_samples/querylang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .querylangParser import querylangParser
else:
    from querylangParser import querylangParser

# This class defines a complete listener for a parse tree produced by querylangParser.
class querylangListener(ParseTreeListener):

    # Enter a parse tree produced by querylangParser#query.
    def enterQuery(self, ctx:querylangParser.QueryContext):
        pass

    # Exit a parse tree produced by querylangParser#query.
    def exitQuery(self, ctx:querylangParser.QueryContext):
        pass


    # Enter a parse tree produced by querylangParser#primary.
    def enterPrimary(self, ctx:querylangParser.PrimaryContext):
        pass

    # Exit a parse tree produced by querylangParser#primary.
    def exitPrimary(self, ctx:querylangParser.PrimaryContext):
        pass


    # Enter a parse tree produced by querylangParser#binaryExpression.
    def enterBinaryExpression(self, ctx:querylangParser.BinaryExpressionContext):
        pass

    # Exit a parse tree produced by querylangParser#binaryExpression.
    def exitBinaryExpression(self, ctx:querylangParser.BinaryExpressionContext):
        pass


    # Enter a parse tree produced by querylangParser#searchCondition.
    def enterSearchCondition(self, ctx:querylangParser.SearchConditionContext):
        pass

    # Exit a parse tree produced by querylangParser#searchCondition.
    def exitSearchCondition(self, ctx:querylangParser.SearchConditionContext):
        pass


    # Enter a parse tree produced by querylangParser#dateSearch.
    def enterDateSearch(self, ctx:querylangParser.DateSearchContext):
        pass

    # Exit a parse tree produced by querylangParser#dateSearch.
    def exitDateSearch(self, ctx:querylangParser.DateSearchContext):
        pass


    # Enter a parse tree produced by querylangParser#binaryDateSearch.
    def enterBinaryDateSearch(self, ctx:querylangParser.BinaryDateSearchContext):
        pass

    # Exit a parse tree produced by querylangParser#binaryDateSearch.
    def exitBinaryDateSearch(self, ctx:querylangParser.BinaryDateSearchContext):
        pass


    # Enter a parse tree produced by querylangParser#dateSearchinfo.
    def enterDateSearchinfo(self, ctx:querylangParser.DateSearchinfoContext):
        pass

    # Exit a parse tree produced by querylangParser#dateSearchinfo.
    def exitDateSearchinfo(self, ctx:querylangParser.DateSearchinfoContext):
        pass


    # Enter a parse tree produced by querylangParser#relativelydate.
    def enterRelativelydate(self, ctx:querylangParser.RelativelydateContext):
        pass

    # Exit a parse tree produced by querylangParser#relativelydate.
    def exitRelativelydate(self, ctx:querylangParser.RelativelydateContext):
        pass


    # Enter a parse tree produced by querylangParser#absolutedate.
    def enterAbsolutedate(self, ctx:querylangParser.AbsolutedateContext):
        pass

    # Exit a parse tree produced by querylangParser#absolutedate.
    def exitAbsolutedate(self, ctx:querylangParser.AbsolutedateContext):
        pass


    # Enter a parse tree produced by querylangParser#pathSearch.
    def enterPathSearch(self, ctx:querylangParser.PathSearchContext):
        pass

    # Exit a parse tree produced by querylangParser#pathSearch.
    def exitPathSearch(self, ctx:querylangParser.PathSearchContext):
        pass


    # Enter a parse tree produced by querylangParser#nameSearch.
    def enterNameSearch(self, ctx:querylangParser.NameSearchContext):
        pass

    # Exit a parse tree produced by querylangParser#nameSearch.
    def exitNameSearch(self, ctx:querylangParser.NameSearchContext):
        pass


    # Enter a parse tree produced by querylangParser#sizeSearch.
    def enterSizeSearch(self, ctx:querylangParser.SizeSearchContext):
        pass

    # Exit a parse tree produced by querylangParser#sizeSearch.
    def exitSizeSearch(self, ctx:querylangParser.SizeSearchContext):
        pass


    # Enter a parse tree produced by querylangParser#typeSearch.
    def enterTypeSearch(self, ctx:querylangParser.TypeSearchContext):
        pass

    # Exit a parse tree produced by querylangParser#typeSearch.
    def exitTypeSearch(self, ctx:querylangParser.TypeSearchContext):
        pass


    # Enter a parse tree produced by querylangParser#durationSearch.
    def enterDurationSearch(self, ctx:querylangParser.DurationSearchContext):
        pass

    # Exit a parse tree produced by querylangParser#durationSearch.
    def exitDurationSearch(self, ctx:querylangParser.DurationSearchContext):
        pass


    # Enter a parse tree produced by querylangParser#metaSearch.
    def enterMetaSearch(self, ctx:querylangParser.MetaSearchContext):
        pass

    # Exit a parse tree produced by querylangParser#metaSearch.
    def exitMetaSearch(self, ctx:querylangParser.MetaSearchContext):
        pass


    # Enter a parse tree produced by querylangParser#quantityCondition.
    def enterQuantityCondition(self, ctx:querylangParser.QuantityConditionContext):
        pass

    # Exit a parse tree produced by querylangParser#quantityCondition.
    def exitQuantityCondition(self, ctx:querylangParser.QuantityConditionContext):
        pass


    # Enter a parse tree produced by querylangParser#contentSearch.
    def enterContentSearch(self, ctx:querylangParser.ContentSearchContext):
        pass

    # Exit a parse tree produced by querylangParser#contentSearch.
    def exitContentSearch(self, ctx:querylangParser.ContentSearchContext):
        pass


    # Enter a parse tree produced by querylangParser#comparison_type.
    def enterComparison_type(self, ctx:querylangParser.Comparison_typeContext):
        pass

    # Exit a parse tree produced by querylangParser#comparison_type.
    def exitComparison_type(self, ctx:querylangParser.Comparison_typeContext):
        pass


    # Enter a parse tree produced by querylangParser#string.
    def enterString(self, ctx:querylangParser.StringContext):
        pass

    # Exit a parse tree produced by querylangParser#string.
    def exitString(self, ctx:querylangParser.StringContext):
        pass


    # Enter a parse tree produced by querylangParser#filename.
    def enterFilename(self, ctx:querylangParser.FilenameContext):
        pass

    # Exit a parse tree produced by querylangParser#filename.
    def exitFilename(self, ctx:querylangParser.FilenameContext):
        pass


    # Enter a parse tree produced by querylangParser#is_or_not.
    def enterIs_or_not(self, ctx:querylangParser.Is_or_notContext):
        pass

    # Exit a parse tree produced by querylangParser#is_or_not.
    def exitIs_or_not(self, ctx:querylangParser.Is_or_notContext):
        pass



del querylangParser