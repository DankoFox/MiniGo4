grammar MiniGo;

// Student ID: 2252360

@lexer::header {
from lexererr import *
}

@lexer::members {

def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preType = None 

def emit(self):
    tk = self.type
    self.preType = tk;
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language = Python3;
}

/****************************************************************************/
/*																	 		*/
/*	                Variables, Constants and Function						*/
/* 																			*/
/****************************************************************************/

program: declList EOF;
declList: decl declList | decl;

decl:
	vardecl
	| constdecl
	| funcdecl
	| structdecl
	| interfacedecl; // LOOKS GOOD ENOUGH

vardecl: // OK
	VAR ID type_ ASSIGN expr SEMICOLON
	| VAR ID type_ SEMICOLON
	| VAR ID ASSIGN expr SEMICOLON;

constdecl: CONST ID ASSIGN expr SEMICOLON; // OK

funcdecl: // OK
	FUNC receiver? ID LPAREN paramList? RPAREN returnType? block SEMICOLON?;
		
receiver: LPAREN ID ID RPAREN;

structdecl: // OK
	TYPE ID STRUCT LBRACE fieldDeclList RBRACE SEMICOLON;

interfacedecl: // OK
	TYPE ID INTERFACE LBRACE methodDeclList RBRACE SEMICOLON;

// DECLARATION-HELPER---------------------------------------------------------------------------
fieldDeclList: fieldDecl fieldDeclList | fieldDecl;
fieldDecl: ID type_ SEMICOLON;

methodDeclList: methodDecl methodDeclList | methodDecl;
methodDecl: ID LPAREN paramList? RPAREN returnType? SEMICOLON;

paramList: param COMMA paramList | param;
param: ID type_ | idList type_;
idList: ID COMMA idList | ID;

returnType: type_;

/****************************************************************************/
/*																	 		*/
/*						EXPRESSION-OK										*/
/* 																			*/
/****************************************************************************/

expr: expr1;

expr1:
	expr1 OR expr2 // Logical OR (Lowest precedence)
	| expr2;

expr2:
	expr2 AND expr3 // Logical AND
	| expr3;

expr3:
	expr3 EQUALS expr4
	| expr3 NOT_EQUALS expr4
	| expr3 LESS_THAN expr4
	| expr3 LESS_THAN_EQ expr4
	| expr3 GREATER_THAN expr4
	| expr3 GREATER_THAN_EQ expr4
	| expr4;

expr4: expr4 ADD expr5 | expr4 SUB expr5 | expr5;

expr5:
	expr5 MUL expr6
	| expr5 DIV expr6
	| expr5 MOD expr6
	| expr6;

expr6:
	NOT expr6 // Logical NOT (Right-to-left)
	| SUB expr6 // Unary Minus (Right-to-left)
	| expr7;

expr7:
	expr7 LBRACKET expr RBRACKET // Array Access
	| expr7 DOT ID LPAREN argList? RPAREN // Method Call
	| expr7 DOT ID // Struct Field Access
	| ID LPAREN argList? RPAREN // Function Call
	| ID
	| literals // (e.g., 42, "Hello", true)
	| LPAREN expr RPAREN; // (Parenthesized Expression)

exprList: expr COMMA exprList | expr;

// LITERALS =======================================

literals:
	integer_literal
	| FLOAT_LITERAL
	| STRING_LITERAL
	| bool_literal
	| array_literal // full form: [3]int{...}
	| struct_literal
	| NIL;

integer_literal: // OK
	DEC_INT_LITERAL
	| OCT_INT_LITERAL
	| HEX_INT_LITERAL
	| BIN_INT_LITERAL;

bool_literal: TRUE | FALSE;

// ARRAY LITERALS --------------------------- arr := [3]int{10, 20, 30}
array_literal: arrayType LBRACE arrayContentList? RBRACE;
arrayContent:
	integer_literal
	| FLOAT_LITERAL
	| STRING_LITERAL
	| bool_literal
	| array_literal_shorthand // inner arrays: {...}
	| struct_literal
	| NIL;

arrayContentList:
	arrayContent COMMA arrayContentList
	| arrayContent;

array_literal_shorthand: LBRACE arrayContentList? RBRACE;

// STRUCT LITERALS -------------------------- Person{name: "Alice", age: 30}
struct_literal: ID LBRACE fieldInitList? RBRACE;
fieldInitList: fieldInit COMMA fieldInitList | fieldInit;
fieldInit: ID COLON expr;

// FUNCTION + METHOD CALLS ========================
functionCall: ID LPAREN argList? RPAREN;
methodCall: expr DOT ID LPAREN argList? RPAREN;

argList: expr COMMA argList | expr;

/****************************************************************************/
/*																	 		*/
/*							STATEMENTS										*/
/* 																			*/
/****************************************************************************/

statement:
	vardecl
	| constdecl
	| assignmentStatement
	| ifStatement
	| forStatement
	| breakStatement
	| continueStatement
	| callStatement
	| returnStatement
	| block
	| expr SEMICOLON;

assignmentStatement: // ok
	expr7 assignmentOperator expr SEMICOLON; // General assignment (e.g., x = 10;)

assignmentOperator: // ok
	DECLARE_ASSIGN
	| ADD_ASSIGN
	| SUB_ASSIGN
	| MUL_ASSIGN
	| DIV_ASSIGN
	| MOD_ASSIGN;

ifStatement: IF expr block elseChain?; // ok

elseChain: ELSE IF expr block elseChain? | ELSE block; // ok

forStatement: FOR (forCondition | forCStyle | forRange) block;

// ok: Condition-based loop: for i < 10 { ... }
forCondition: expr;

// ok: Classic C-style loop: for i := 0; i < 10; i += 1 { ... }
forCStyle:
    init SEMICOLON expr SEMICOLON update; 

init:
    VAR ID type_? ASSIGN expr
    | assignExpr;

update:
    assignExpr;

assignExpr:
    expr7 assignmentOperator expr;

// ok: Range-based loop: - for index, value := range arr { ... } - for _, value := range arr { ... }
forRange: (ID COMMA ID ':=' RANGE expr) // Index and value
	| ('_' COMMA ID ':=' RANGE expr); // Ignore index

breakStatement: BREAK SEMICOLON; // ok
continueStatement: CONTINUE SEMICOLON; // ok
callStatement: ( functionCall | methodCall) SEMICOLON; // ok
returnStatement: RETURN expr? SEMICOLON; // ok

block: LBRACE statementList RBRACE SEMICOLON?; // ok
statementList: statement statementList | statement;

/****************************************************************************/
/*																	 		*/
/*								TYPE										*/
/* 																			*/
/****************************************************************************/
type_:
	primitiveType
	| arrayType
	| structType
	| interfaceType; // OK

primitiveType: INT | FLOAT | BOOLEAN | STRING; // OK

arrayType: LBRACKET (integer_literal | ID) RBRACKET type_; // OK

structType: ID; // they're just names

interfaceType: ID; // they're just names
/****************************************************************************/
/*																	 		*/
/*								LEXER										*/
/* 																			*/
/****************************************************************************/

LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;

// Keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
TRUE: 'true';
FALSE: 'false';
NIL: 'nil';

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUALS: '==';
NOT_EQUALS: '!=';
LESS_THAN: '<';
LESS_THAN_EQ: '<=';
GREATER_THAN: '>';
GREATER_THAN_EQ: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
DECLARE_ASSIGN: ':=';

// Separators
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';
COMMA: ',';
SEMICOLON: ';';
COLON: ':';
DOT: '.';

SEMICOLON_NEWLINE:
	SEMICOLON
	| '\r'? '\n' {
        if self.preType in {
            self.ID, 
			self.INT, self.FLOAT, self.BOOLEAN, self.STRING,
			self.DEC_INT_LITERAL, self.OCT_INT_LITERAL,
			self.HEX_INT_LITERAL, self.BIN_INT_LITERAL,
			self.FLOAT_LITERAL, self.TRUE, self.FALSE,
			self.STRING_LITERAL, 
            self.RETURN, self.CONTINUE, self.BREAK,
            self.RPAREN, self.RBRACKET, self.RBRACE
        }:
            self.type = self.SEMICOLON;
            self.text = ';';
        else:
            self.skip();
    };

DEC_INT_LITERAL: '0' | [1-9] [0-9]*;
OCT_INT_LITERAL: '0' [oO] [0-7]+;
HEX_INT_LITERAL: '0' [xX] [0-9a-fA-F]+;
BIN_INT_LITERAL: '0' [bB] [01]+;

fragment DIGIT: [0-9];
fragment EXPONENT_PART: [eE] [+-]? DIGIT+;
FLOAT_LITERAL:
	DIGIT+ '.' DIGIT* EXPONENT_PART?
	| '.' DIGIT+ EXPONENT_PART?;

ID: [a-zA-Z_][a-zA-Z0-9_]*;

fragment STR_CHAR: ~[\r\n"\\] | ESC_SEQ;
fragment ESC_SEQ: '\\' [tnr"\\];
STRING_LITERAL: '"' STR_CHAR* '"';

UNCLOSE_STRING:
	'"' STR_CHAR* ('\r\n' | '\n' | EOF) {
	if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
		raise UncloseString(self.text[:-2])
	elif (self.text[-1] == '\n'):
		raise UncloseString(self.text[:-1])
	else:
		raise UncloseString(self.text[:])
};

fragment ESC_ILLEGAL: '\\' ~[tnr"\\];
ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
	raise IllegalEscape(self.text[:])
};

NL: '\n'; //skip newlines
WS: [ \t\r]+ -> skip; // skip spaces, tabs

ERROR_CHAR: .;