
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUMBER ID WHITESPACE ENTER EQ COL PLUS MINUS TIMES DIVIDE LPAREN RPAREN LBRACE RBRACE ARROW COMMA TRIPLEDOT FUNC VAR FOR TYPE TYPE IN TYPEstart : statements\n\t\t\t| emptyempty :statements : statement ENTER next_statementnext_statement : statement ENTER next_statement\n\t\t\t\t\t| emptystatement : assignment_statement\n\t\t\t\t| declaration_statement\n\t\t\t\t| function_defination\n\t\t\t\t| for_loopassignment_statement : ID WHITESPACE EQ WHITESPACE expressiondeclaration_statement : VAR WHITESPACE ID COL WHITESPACE TYPE\n\t\t\t\t\t\t\t| VAR WHITESPACE ID COL WHITESPACE TYPE WHITESPACE EQ WHITESPACE expression\n\t\t\t\t\t\t\t| VAR WHITESPACE ID WHITESPACE EQ WHITESPACE expression expression : expression PLUS term\n\t\t\t\t| expression MINUS term\n\t\t\t\t| term\n\t\t\t\tterm : term TIMES factor\n\t\t\t| term DIVIDE factor\n\t\t\t| factor\n\tfactor : ID\n\t\t\t| NUMBER\n\tfunction_defination : FUNC WHITESPACE ID LPAREN optional_parameters RPAREN WHITESPACE optional_return_type WHITESPACE LBRACE ENTER statements RBRACEoptional_parameters : has_parameter\n\t\t\t\t\t\t| emptyhas_parameter : has_parameter COMMA has_parameter\n\t\t\t\t\t\t| ID COL TYPEoptional_return_type : ARROW WHITESPACE TYPEfor_loop : FOR WHITESPACE ID WHITESPACE IN WHITESPACE NUMBER TRIPLEDOT NUMBER WHITESPACE LBRACE ENTER statements RBRACE'
    
_lr_action_items = {'ID':([0,14,15,16,17,25,28,29,44,45,46,47,48,52,68,76,79,],[1,19,20,1,24,31,38,1,31,31,31,31,31,38,31,1,1,]),'DIVIDE':([31,32,33,35,54,55,56,57,],[-21,-22,44,-20,-19,-18,44,44,]),'TRIPLEDOT':([63,],[67,]),'ENTER':([3,4,5,7,10,22,31,32,33,34,35,49,54,55,56,57,58,72,73,77,80,82,],[-7,-10,-9,-8,16,29,-21,-22,-17,-11,-20,-12,-19,-18,-16,-15,-14,-13,76,79,-23,-29,]),'IN':([30,],[43,]),'COMMA':([40,60,62,],[52,-27,52,]),'NUMBER':([25,44,45,46,47,48,53,67,68,],[32,32,32,32,32,32,63,71,32,]),'VAR':([0,16,29,76,79,],[2,2,2,2,2,]),'TYPE':([37,50,70,],[49,60,74,]),'RBRACE':([16,21,23,29,42,78,81,],[-3,-6,-4,-3,-5,80,82,]),'RPAREN':([28,39,40,41,60,62,],[-3,51,-24,-25,-27,-26,]),'WHITESPACE':([1,2,9,12,18,19,24,27,36,43,49,51,64,65,66,71,74,],[13,14,15,17,25,26,30,37,48,53,59,61,68,69,70,75,-28,]),'LPAREN':([20,],[28,]),'PLUS':([31,32,33,34,35,54,55,56,57,58,72,],[-21,-22,-17,47,-20,-19,-18,-16,-15,47,47,]),'FUNC':([0,16,29,76,79,],[9,9,9,9,9,]),'EQ':([13,26,59,],[18,36,64,]),'$end':([0,6,8,11,16,21,23,29,42,],[-3,-1,-2,0,-3,-6,-4,-3,-5,]),'TIMES':([31,32,33,35,54,55,56,57,],[-21,-22,45,-20,-19,-18,45,45,]),'LBRACE':([69,75,],[73,77,]),'COL':([19,38,],[27,50,]),'ARROW':([61,],[66,]),'FOR':([0,16,29,76,79,],[12,12,12,12,12,]),'MINUS':([31,32,33,34,35,54,55,56,57,58,72,],[-21,-22,-17,46,-20,-19,-18,-16,-15,46,46,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'optional_parameters':([28,],[39,]),'empty':([0,16,28,29,],[8,21,41,21,]),'optional_return_type':([61,],[65,]),'has_parameter':([28,52,],[40,62,]),'start':([0,],[11,]),'assignment_statement':([0,16,29,76,79,],[3,3,3,3,3,]),'for_loop':([0,16,29,76,79,],[4,4,4,4,4,]),'statement':([0,16,29,76,79,],[10,22,22,10,10,]),'function_defination':([0,16,29,76,79,],[5,5,5,5,5,]),'next_statement':([16,29,],[23,42,]),'statements':([0,76,79,],[6,78,81,]),'declaration_statement':([0,16,29,76,79,],[7,7,7,7,7,]),'term':([25,46,47,48,68,],[33,56,57,33,33,]),'expression':([25,48,68,],[34,58,72,]),'factor':([25,44,45,46,47,48,68,],[35,54,55,35,35,35,35,]),}

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
  ('statement -> assignment_statement','statement',1,'p_statement','swift_parser.py',41),
  ('statement -> declaration_statement','statement',1,'p_statement','swift_parser.py',42),
  ('statement -> function_defination','statement',1,'p_statement','swift_parser.py',43),
  ('statement -> for_loop','statement',1,'p_statement','swift_parser.py',44),
  ('assignment_statement -> ID WHITESPACE EQ WHITESPACE expression','assignment_statement',5,'p_assignment_statement','swift_parser.py',48),
  ('declaration_statement -> VAR WHITESPACE ID COL WHITESPACE TYPE','declaration_statement',6,'p_declaration_statement','swift_parser.py',59),
  ('declaration_statement -> VAR WHITESPACE ID COL WHITESPACE TYPE WHITESPACE EQ WHITESPACE expression','declaration_statement',10,'p_declaration_statement','swift_parser.py',60),
  ('declaration_statement -> VAR WHITESPACE ID WHITESPACE EQ WHITESPACE expression','declaration_statement',7,'p_declaration_statement','swift_parser.py',61),
  ('expression -> expression PLUS term','expression',3,'p_expression','swift_parser.py',87),
  ('expression -> expression MINUS term','expression',3,'p_expression','swift_parser.py',88),
  ('expression -> term','expression',1,'p_expression','swift_parser.py',89),
  ('term -> term TIMES factor','term',3,'p_term','swift_parser.py',101),
  ('term -> term DIVIDE factor','term',3,'p_term','swift_parser.py',102),
  ('term -> factor','term',1,'p_term','swift_parser.py',103),
  ('factor -> ID','factor',1,'p_factor','swift_parser.py',115),
  ('factor -> NUMBER','factor',1,'p_factor','swift_parser.py',116),
  ('function_defination -> FUNC WHITESPACE ID LPAREN optional_parameters RPAREN WHITESPACE optional_return_type WHITESPACE LBRACE ENTER statements RBRACE','function_defination',13,'p_function_defination','swift_parser.py',121),
  ('optional_parameters -> has_parameter','optional_parameters',1,'p_optional_parameters','swift_parser.py',129),
  ('optional_parameters -> empty','optional_parameters',1,'p_optional_parameters','swift_parser.py',130),
  ('has_parameter -> has_parameter COMMA has_parameter','has_parameter',3,'p_has_parameter','swift_parser.py',137),
  ('has_parameter -> ID COL TYPE','has_parameter',3,'p_has_parameter','swift_parser.py',138),
  ('optional_return_type -> ARROW WHITESPACE TYPE','optional_return_type',3,'p_optional_return_type','swift_parser.py',147),
  ('for_loop -> FOR WHITESPACE ID WHITESPACE IN WHITESPACE NUMBER TRIPLEDOT NUMBER WHITESPACE LBRACE ENTER statements RBRACE','for_loop',14,'p_for_loop','swift_parser.py',153),
]
