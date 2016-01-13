

input : namespace_declaration_opt  using_namespace_list_opt  function_declaration_list


# namespace 

namespace_declaration_opt : namespace_declaration
	| empty

namespace_declaration : NAMESPACE  qualified_identifier ';'

qualified_identifier : ID
	| qualified_identifier  '.' ID

using_namespace_list_opt : using_namespace_list
	| empty

using_namespace_list : using_namespace
	| using_namespace_list using_namespace

using_namespace : USING  qualified_identifier ';'



# function

function_declaration_list : function_declaration
	| function_declaration_list  function_declaration
    	
function_declaration : function_header   function_body


function_header :  function_modifier_opt  return_type  ID '(' fixed_parameters_opt ')'

function_modifier_opt : function_modifier
	| empty

function_modifier : PUBLIC
	| PRIVATE

return_type : type
	| VOID

fixed_parameters_opt : fixed_parameters
	| empty

fixed_parameters : fixed_parameter
	| fixed_parameters ',' fixed_parameter

fixed_parameter :  type  ID

function_body : block

# type

type : INT
	| DOUBLE
	| BOOL

# Statements

block : '{' statement_list_opt '}'

statement_list_opt : statement_list
	| empty

statement_list : statement
	| statement_list   statement

statement: labeled_statement
	| declaration_statement
	| embedded_statement

embedded_statement : block
	| empty_statement
	| expression_statement
	| selection_statement
	| iteration_statement
	| jump_statement

empty_statement : ';'

labeled_statement : ID  ':'  statement


declaration_statement : local_variable_declaration   ';'
	| local_constant_declaration   ';'















# other

empty : 
