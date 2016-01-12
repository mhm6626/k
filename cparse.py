# -----------------------------------------------------------------------------
# cparse.py
#
# Simple parser for ANSI C.  Based on the grammar in K&R, 2nd Ed.
# -----------------------------------------------------------------------------

import sys
import clex
import ply.yacc as yacc

# Get the token map
tokens = clex.tokens



def p_input(p):
    """
    input : namespace_declaration_opt  using_namespace_list_opt  function_declaration_list
    """
    pass

######################################
# namespace
###

def p_namespace_declaration_opt(p):
    """
    namespace_declaration_opt : namespace_declaration
        | empty
    """
    pass

def p_namespace_declaration(p):
    """
    namespace_declaration : NAMESPACE  qualified_identifier ';'
    """
    pass

def p_qualified_identifier(p):
    """
    qualified_identifier : ID
        | qualified_identifier  '.' ID
    """
    pass

def p_using_namespace_list_opt(p):
    """
    using_namespace_list_opt : using_namespace_list
        | empty
    """
    pass

def p_using_namespace_list(p):
    """
    using_namespace_list : using_namespace
        | using_namespace_list using_namespace
    """
    pass

def p_using_namespace(p):
    """
    using_namespace : USING  qualified_identifier ';'
    """
    pass

######################################
# function
###

def p_function_declaration_list(p):
    """
    function_declaration_list : function_declaration
        | function_declaration_list  function_declaration
    """
    pass

def p_function_declaration(p):
    """
    function_declaration : function_header   function_body
    """
    pass

def p_function_header(p):
    """
    function_header :  function_modifier_opt  return_type  ID '(' fixed_parameters_opt ')'
    """
    pass

def p_function_modifier_opt(p):
    """
    function_modifier_opt : function_modifier
        | empty
    """
    pass

def p_function_modifier(p):
    """
    function_modifier : PUBLIC
        | PRIVATE
    """
    pass

def p_return_type(p):
    """
    return_type : type
        | VOID
    """
    pass

def p_fixed_parameters_opt(p):
    """
    fixed_parameters_opt : fixed_parameters
        | empty
    """
    pass

def p_fixed_parameters(p):
    """
    fixed_parameters : fixed_parameter
        | fixed_parameters ',' fixed_parameter
    """
    pass

def p_fixed_parameter(p):
    """
    fixed_parameter :  type  ID
    """
    pass

def p_function_body(p):
    """
    function_body : block
    """
    pass

######################################
# type
###

def p_type(p):
    """
    type : INT
        | DOUBLE
        | BOOL
    """
    pass

######################################
# block
###

def p_block(p):
    """
    block : '{' ID '}'
    """
    pass

######################################
# other
###

def p_empty(p):
    """
    empty :
    """
    pass



def p_error(t):
    print("Whoa. We're hosed")

import profile
# Build the grammar

yacc.yacc()
#yacc.yacc(method='LALR',write_tables=False,debug=True)

#profile.run("yacc.yacc(method='LALR')")




