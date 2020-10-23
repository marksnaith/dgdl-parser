/*
Copyright (C) 2020  Centre for Argument Technology (http://arg.tech)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

grammar dgdl;

game :
    'game' '(' 'id' ':' gameID ')' '{' composition (rules)* (interaction)+ '}' EOF;

gameID : identifier;

composition: roleList? participants player+ store* turntaking? backtrack? extURI*;

roleList :
    'roles' '(' role (',' role)* ')';

role : (LISTENER | SPEAKER | identifier);

participants :
    'participants' '(' 'min' ':' minplayers ',' 'max' ':' maxplayers ')';

player :
    'player' '(' 'id' ':' playerID (',' playerRoleList)? (',' 'min' ':' minplayers)? (',' 'max' ':' maxplayers)? ')';

playerID : identifier;

playerRoleList :
    'roles' ':' '{' role (',' role)* '}';

store :
    'store' '(' 'id' ':' storeID ',' 'owner' ':' storeOwner ',' 'structure' ':' storeStructure ',' 'visibility' ':' storeVisibility (',' storeContent)? ')';

storeID : identifier;

storeOwner :
    (identifier | '{' identifier (',' identifier)+ '}');

storeStructure :
    (SET | QUEUE | STACK);

storeVisibility :
    (PUBLIC | PRIVATE);

storeContent :
    '{' (contentVar | STRINGLITERAL) (',' (contentVar| STRINGLITERAL))* '}';

turntaking :
    'turntaking' '(' turntakingtype ')';

turntakingtype : ('strict' | 'liberal');

backtrack :
    'backtracking' '(' onoff ')';

onoff : ('on' | 'off');

extURI:
    'extURI' '(' 'id' ':' extUriID ',' 'uri' ':' uri ')';

uri : STRINGLITERAL;

extUriID : identifier;

minplayers : number;
maxplayers : (number | 'undefined');

rules :
    'rule' '(' 'id' ':' ruleID ',' 'scope' ':' scopeType ')' ruleBody;

ruleID : identifier;

scopeType :
    (INITIAL | TURNWISE | MOVEWISE);

ruleBody :
    '{' (effects (conditional)? | conditional) '}';

effects :
    effect+; // (effect)*;

effect :
    (move | storeOp | statusUpdate | roleAssignment | save) ';';

move :
  'move' '(' moveaction ',' movetime ',' moveID (',' addressee)? (',' content)? (',' user)? ')';

moveaction : ('add' | 'delete');

movetime : ('next' | 'future');

moveID : identifier;

addressee : '$' identifier;

content :
    '{' (contentVar | runtimeVar) (',' contentVar | runtimeVar)* '}';

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

save :
    'save' '(' storeContent ',' runtimeVar ')';

runtimeVar :
    '$' identifier '$';

conditional :
    'if' '(' requirements ')' '{' effects '}' condelseif? condelse? ';'?;

requirements :
    (condition (AMPAND condition)* );

condition :
    NEG? (event | roleInspection | storeInspection | uriTest);

event :
    'event' '(' eventpos ',' moveID  (',' eventContent)? (',' user)? ')';

eventpos :
    ('last' | 'past');

eventContent :
    '{' (runtimeVar | STRINGLITERAL) (',' runtimeVar | STRINGLITERAL)* '}';

roleInspection :
    'inrole' '(' playerID ',' role ')';

storeInspection :
    'inspect' '(' storepos ',' storeContent ',' storeID (',' user)? (',' storetime)? ')';

storepos : ('in' | 'on' | 'top' );

storetime : ('initial' | 'past' | 'current');

uriTest :
    'uriTest' '(' extUriID ')';

condelseif :
    'elseif ' requirements 'then' '{' effects '}' condelseif? condelse?;

condelse : 'else' '{' effects '}';

/* === Interactions === */

interaction :
    'interaction' '(' 'id' ':' moveID (',' 'addressee' ':' user)? (',' 'content' ':' content)? (',' 'opener' ':' opener)? ')' ruleBody;

opener : STRINGLITERAL;

/* Temporary for MWE */


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

AMPAND : '&&';
NEG : '!';

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
