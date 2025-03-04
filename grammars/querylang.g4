grammar querylang;

query: primary EOF;   

primary:
    binaryExpression (SPACE 'AND' SPACE binaryExpression | SPACE 'OR' SPACE binaryExpression)*
    ;

binaryExpression:
    '('primary')'
    | searchCondition
    ;

searchCondition:
    dateSearch
    | pathSearch
    | nameSearch
    | sizeSearch
    | typeSearch
    | durationSearch
    | metaSearch
    | quantityCondition
    | contentSearch
    ;

dateSearch: 
    binaryDateSearch (SPACE 'AND' SPACE binaryDateSearch | SPACE 'OR' SPACE binaryDateSearch)*
    ;

binaryDateSearch:
    '('dateSearchinfo')'
    | dateSearchinfo
    ;

dateSearchinfo: 
    'DATE' SPACE comparison_type SPACE absolutedate
    | 'DATE' SPACE comparison_type SPACE relativelydate
    ;
relativelydate: 'CURRENT' SPACE '-' SPACE string;
absolutedate: STRING_VALUE;

pathSearch: 'PATH' SPACE is_or_not SPACE string;
nameSearch: 'NAME' SPACE 'CONTAINS' SPACE string;
sizeSearch:
    'SIZE' SPACE comparison_type SPACE string
    | 'SIZE' SPACE comparison_type SPACE 'FILE_SIZE' SPACE filename;
typeSearch: 'TYPE' SPACE is_or_not SPACE string;
durationSearch: 'DURATION' SPACE comparison_type SPACE string;
metaSearch:
    'META_TYPE' SPACE 'IS' SPACE string SPACE 'WITH' SPACE 'META_VALUE' SPACE is_or_not SPACE string;
quantityCondition: 'QUANTITY' SPACE '=' SPACE NUMBER_VALUE;
contentSearch:
    'CONTENT' SPACE 'CONTAINS' SPACE string
    | 'CONTENT' SPACE 'EQUALS' SPACE 'FILE' SPACE filename;

comparison_type: '=' | '<' | '>' | '!=' | '<=' | '>=';


string: STRING_VALUE;
filename: STRING_VALUE;

SPACE: ' ';
STRING_VALUE: '"' .*? '"';
is_or_not: 'IS' | 'IS NOT';
NUMBER_VALUE: [0-9]+;
