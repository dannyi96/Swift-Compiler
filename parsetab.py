
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUMBER ID WHITESPACE ENTER EQ COL PLUS MINUS TIMES DIVIDE LPAREN RPAREN LBRACE RBRACE ARROW COMMA TRIPLEDOT TYPE TYPE FUNC TYPE FOR IN VARstart : statements\n\t\t\t| emptyempty :statements : statement ENTER next_statementnext_statement : statement ENTER next_statement\n\t\t\t\t\t| emptystatement : assignment_statement\n\t\t\t\t| declaration_statement\n\t\t\t\t| function_defination\n\t\t\t\t| for_loopassignment_statement : ID WHITESPACE EQ WHITESPACE expressiondeclaration_statement : VAR WHITESPACE ID COL WHITESPACE TYPE\n\t\t\t\t\t\t\t| VAR WHITESPACE ID COL WHITESPACE TYPE WHITESPACE EQ WHITESPACE expression\n\t\t\t\t\t\t\t| VAR WHITESPACE ID WHITESPACE EQ WHITESPACE expression expression : expression PLUS term\n\t\t\t\t| expression MINUS term\n\t\t\t\t| term\n\t\t\t\tterm : term TIMES factor\n\t\t\t| term DIVIDE factor\n\t\t\t| factor\n\tfactor : ID\n\t\t\t| NUMBER\n\tfunction_defination : FUNC WHITESPACE ID LPAREN optional_parameters RPAREN WHITESPACE optional_return_type WHITESPACE LBRACE ENTER statements RBRACEoptional_parameters : has_parameter\n\t\t\t\t\t\t| emptyhas_parameter : has_parameter COMMA has_parameter\n\t\t\t\t\t\t| ID COL WHITESPACE TYPEoptional_return_type : ARROW WHITESPACE TYPEfor_loop : FOR WHITESPACE ID WHITESPACE IN WHITESPACE NUMBER TRIPLEDOT NUMBER WHITESPACE LBRACE ENTER statements RBRACE'
    
_lr_action_items = {'LBRACE':([71,73,],[75,77,]),'ID':([0,14,15,16,17,25,26,30,44,45,46,47,49,53,70,78,79,],[3,3,22,23,24,34,3,41,34,34,34,34,34,41,34,3,3,]),'$end':([0,2,8,12,14,19,21,26,36,],[-3,-2,-1,0,-3,-6,-4,-3,-5,]),'LPAREN':([24,],[30,]),'PLUS':([31,32,33,34,35,54,55,56,57,59,74,],[45,-20,-17,-21,-22,-16,-15,-18,-19,45,45,]),'EQ':([13,28,60,],[18,38,65,]),'ARROW':([62,],[68,]),'TYPE':([39,61,72,],[50,66,76,]),'VAR':([0,14,26,78,79,],[9,9,9,9,9,]),'FUNC':([0,14,26,78,79,],[10,10,10,10,10,]),'COL':([23,41,],[29,51,]),'MINUS':([31,32,33,34,35,54,55,56,57,59,74,],[44,-20,-17,-21,-22,-16,-15,-18,-19,44,44,]),'NUMBER':([25,44,45,46,47,48,49,64,70,],[35,35,35,35,35,58,35,69,35,]),'ENTER':([1,4,5,7,11,20,31,32,33,34,35,50,54,55,56,57,59,74,75,77,82,83,],[-8,14,-9,-10,-7,26,-11,-20,-17,-21,-22,-12,-16,-15,-18,-19,-14,-13,78,79,-23,-29,]),'RPAREN':([30,40,42,43,63,66,],[-3,-25,52,-24,-26,-27,]),'DIVIDE':([32,33,34,35,54,55,56,57,],[-20,47,-21,-22,47,47,-18,-19,]),'COMMA':([43,63,66,],[53,53,-27,]),'FOR':([0,14,26,78,79,],[6,6,6,6,6,]),'TIMES':([32,33,34,35,54,55,56,57,],[-20,46,-21,-22,46,46,-18,-19,]),'WHITESPACE':([3,6,9,10,18,22,23,29,37,38,50,51,52,65,67,68,69,76,],[13,15,16,17,25,27,28,39,48,49,60,61,62,70,71,72,73,-28,]),'IN':([27,],[37,]),'RBRACE':([14,19,21,26,36,80,81,],[-3,-6,-4,-3,-5,82,83,]),'TRIPLEDOT':([58,],[64,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaration_statement':([0,14,26,78,79,],[1,1,1,1,1,]),'expression':([25,49,70,],[31,59,74,]),'assignment_statement':([0,14,26,78,79,],[11,11,11,11,11,]),'optional_return_type':([62,],[67,]),'statement':([0,14,26,78,79,],[4,20,20,4,4,]),'start':([0,],[12,]),'has_parameter':([30,53,],[43,63,]),'function_defination':([0,14,26,78,79,],[5,5,5,5,5,]),'next_statement':([14,26,],[21,36,]),'optional_parameters':([30,],[42,]),'empty':([0,14,26,30,],[2,19,19,40,]),'for_loop':([0,14,26,78,79,],[7,7,7,7,7,]),'statements':([0,78,79,],[8,80,81,]),'factor':([25,44,45,46,47,49,70,],[32,32,32,56,57,32,32,]),'term':([25,44,45,49,70,],[33,54,55,33,33,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> statements','start',1,'p_start','swift_parser.py',20),
  ('start -> empty','start',1,'p_start','swift_parser.py',21),
  ('empty -> <empty>','empty',0,'p_empty','swift_parser.py',25),
  ('statements -> statement ENTER next_statement','statements',3,'p_statements','swift_parser.py',29),
  ('next_statement -> statement ENTER next_statement','next_statement',3,'p_next_statement','swift_parser.py',33),
  ('next_statement -> empty','next_statement',1,'p_next_statement','swift_parser.py',34),
  ('statement -> assignment_statement','statement',1,'p_statement','swift_parser.py',42),
  ('statement -> declaration_statement','statement',1,'p_statement','swift_parser.py',43),
  ('statement -> function_defination','statement',1,'p_statement','swift_parser.py',44),
  ('statement -> for_loop','statement',1,'p_statement','swift_parser.py',45),
  ('assignment_statement -> ID WHITESPACE EQ WHITESPACE expression','assignment_statement',5,'p_assignment_statement','swift_parser.py',49),
  ('declaration_statement -> VAR WHITESPACE ID COL WHITESPACE TYPE','declaration_statement',6,'p_declaration_statement','swift_parser.py',60),
  ('declaration_statement -> VAR WHITESPACE ID COL WHITESPACE TYPE WHITESPACE EQ WHITESPACE expression','declaration_statement',10,'p_declaration_statement','swift_parser.py',61),
  ('declaration_statement -> VAR WHITESPACE ID WHITESPACE EQ WHITESPACE expression','declaration_statement',7,'p_declaration_statement','swift_parser.py',62),
  ('expression -> expression PLUS term','expression',3,'p_expression','swift_parser.py',88),
  ('expression -> expression MINUS term','expression',3,'p_expression','swift_parser.py',89),
  ('expression -> term','expression',1,'p_expression','swift_parser.py',90),
  ('term -> term TIMES factor','term',3,'p_term','swift_parser.py',102),
  ('term -> term DIVIDE factor','term',3,'p_term','swift_parser.py',103),
  ('term -> factor','term',1,'p_term','swift_parser.py',104),
  ('factor -> ID','factor',1,'p_factor','swift_parser.py',116),
  ('factor -> NUMBER','factor',1,'p_factor','swift_parser.py',117),
  ('function_defination -> FUNC WHITESPACE ID LPAREN optional_parameters RPAREN WHITESPACE optional_return_type WHITESPACE LBRACE ENTER statements RBRACE','function_defination',13,'p_function_defination','swift_parser.py',122),
  ('optional_parameters -> has_parameter','optional_parameters',1,'p_optional_parameters','swift_parser.py',129),
  ('optional_parameters -> empty','optional_parameters',1,'p_optional_parameters','swift_parser.py',130),
  ('has_parameter -> has_parameter COMMA has_parameter','has_parameter',3,'p_has_parameter','swift_parser.py',133),
  ('has_parameter -> ID COL WHITESPACE TYPE','has_parameter',4,'p_has_parameter','swift_parser.py',134),
  ('optional_return_type -> ARROW WHITESPACE TYPE','optional_return_type',3,'p_optional_return_type','swift_parser.py',137),
  ('for_loop -> FOR WHITESPACE ID WHITESPACE IN WHITESPACE NUMBER TRIPLEDOT NUMBER WHITESPACE LBRACE ENTER statements RBRACE','for_loop',14,'p_for_loop','swift_parser.py',140),
]
