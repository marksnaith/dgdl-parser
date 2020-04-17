/*
* Grammar for the Dialogue Game Description Language v2.0
* Mark Snaith
* (c) 2020 Centre for Argument Technology, University of Dundee, Dundee, UK, DD1 4HN
*/

grammar dgdl;

system :
    ( systemID '{' (game)+ '}') EOF;

systemID : identifier;

game :
    gameID '{' composition (rules)* (interaction)+ '}';

gameID : identifier;

composition: roleList? participants player+ store* backtrack?;

roleList :
    'roles' '{' role (',' role)* '}';

role : (LISTENER | SPEAKER | identifier);

participants :
    'participants' '{' 'min' ':' minplayers ',' 'max' ':' maxplayers '}';

player :
    'player' '{' 'id' ':' playerID (',' roleList)? (',' 'min' ':' minplayers)? (',' 'max' ':' maxplayers)? '}';

playerID : identifier;

store :
    'store' '{' 'id' ':' storeID ',' 'owner' ':' storeOwner ',' 'structure' ':' storeStructure ',' 'visibility' ':' storeVisibility (',' storeContent)? '}';

storeID : identifier;

storeOwner :
    (identifier | '{' identifier (',' identifier)+ '}');

storeStructure :
    (SET | QUEUE | STACK);

storeVisibility :
    (PUBLIC | PRIVATE);

storeContent :
    '{' identifier (',' identifier)* '}';
backtrack :
    'backtracking' '{' onoff '}';

onoff : ('on' | 'off');

minplayers : number;
maxplayers : (number | 'undefined');


rules :
    'rule' '{' 'id' ':' ruleID ',' 'scope' ':' scopeType ',' ruleBody '}';

ruleID : identifier;

scopeType :
    (INITIAL | TURNWISE | MOVEWISE);

ruleBody :
    '{' (effects ('&' conditional)? | conditional) '}';

effects :
    effect ('&' effect)*;

effect :
    (move | storeOp | statusUpdate | roleAssignment);

move :
  'move' '(' moveaction ',' movetime ',' moveID (',' addressee)? (',' content)? (',' user)? ')';

moveaction : ('add' | 'delete');

movetime : ('next' | 'future');

moveID : identifier;

addressee : '$' identifier;

content :
    '{' contentVar (',' contentVar)* '}';

storeOp :
    'store' '(' storeaction ',' storeContent ',' storeID ')';

storeaction : ('add' | 'remove' | 'empty');

statusUpdate :
    'status' '(' status ',' identifier ')';

status :
    ('active' | 'inactive' | 'complete' | 'incomplete' | 'terminate');

roleAssignment : (assignment | unassignment);

assignment :
    'assign' '(' user ',' role ')';

unassignment :
    'unassign' '(' user ',' role ')';

user : identifier;

conditional : 'conditional';

/* Temporary for MWE */
interaction: identifier;

/* Common rules */

upperChar : UpperChar;
lowerChar : LowerChar;
identifier : Identifier;
number : Number;

contentVar : LowerChar;

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
