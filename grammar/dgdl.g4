/*
* Grammar for the Dialogue Game Description Language v2.0
* Mark Snaith
* (c) 2009 Centre for Argument Technology, University of Dundee, Dundee, UK, DD1 4HN
*/

grammar dgdl;

system :
    ( systemID '{' (game)+ '}') EOF;

systemID : identifier;

game :
    gameID '{' composition (rules)* (interaction)+ '}';

gameID : identifier;

/* Temporary for MWE */
composition: identifier;
rules: identifier;
interaction: identifier;

/* Common rules */

upperChar : UpperChar;
lowerChar : LowerChar;
identifier : Identifier;
number : Number;

Identifier : UpperChar (UpperChar | LowerChar | Number)+;
LowerChar : 'a'..'z';
UpperChar : 'A'..'Z';
Number : '0'..'9' ('0'..'9')*;

/* Lexer */
WS          : (' ' | '\r' | '\t' | '\u000C' | '\n')+ -> channel(HIDDEN);

MOVEACTION : ('add' | 'remove');
MOVETIME : ('next' | 'future');

ONOFF        : 'on' | 'off';
LISTENER  : 'listener';
SPEAKER   : 'speaker';
INITIAL : 'initial';
TURNWISE : 'turnwise';
MOVEWISE : 'movewise';
SET      : 'set';
QUEUE    : 'queue';
STACK    : 'stack';
PUBLIC    : 'public';
PRIVATE    : 'private';
STRINGLITERAL   : '"' (~( '\\' | '"' | '\r' | '\n' ))* '"';
COMMENT : '/*' .*? '*/' -> channel(HIDDEN);
LINE_COMMENT : '//' ~('\n'|'\r')* '\r'? '\n' -> channel(HIDDEN);
