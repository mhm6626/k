##################################################
# C.2.1 Basic concepts

def p_namespace_name(p):
    """
    namespace_name : namespace_or_type_name  
    """
    pass


def p_type_name(p):
    """
    type_name : namespace_or_type_name  
    """
    pass


def p_namespace_or_type_name(p):
    """
    namespace_or_type_name : identifier  
                           | namespace_or_type_name  PERIOD  identifier  
    
    """
    pass


##################################################
# C.2.2 Types


def p_type(p):
    """
    type : value_type  
         | reference_type  
    """
    pass


def p_value_type(p):
    """
    value_type : struct_type  
               | enum_type  
    """
    pass


def p_struct_type(p):
    """
    struct_type : type_name  
                | simple_type  
    """
    pass


def p_simple_type(p):
    """
    simple_type : numeric_type  
                | BOOL  
    """
    pass


def p_numeric_type(p):
    """
    numeric_type : integral_type  
                 | floating_point_type  
                 | DECIMAL  
    """
    pass


def p_integral_type(p):
    """
    integral_type : SBYTE  
                  | BYTE  
                  | SHORT  
                  | USHORT  
                  | INT  
                  | UINT  
                  | LONG  
                  | ULONG  
                  | CHAR  
    """
    pass


def p_floating_point_type(p):
    """
    floating_point_type : FLOAT  
                        | DOUBLE  
    """
    pass


def p_enum_type(p):
    """
    enum_type : type_name  
    """
    pass


def p_reference_type(p):
    """
    reference_type : class_type  
                   | interface_type  
                   | array_type  
                   | delegate_type  
    """
    pass


def p_class_type(p):
    """
    class_type : type_name  
               | OBJECT  
               | STRING  
    """
    pass


def p_interface_type(p):
    """
    interface_type : type_name  
    """
    pass


def p_array_type(p):
    """
    array_type : non_array_type  rank_specifiers  
    """
    pass


def p_non_array_type(p):
    """
    non_array_type : type  
    """
    pass


def p_rank_specifiers(p):
    """
    rank_specifiers : rank_specifier  
                    | rank_specifiers  rank_specifier  
    """
    pass


def p_rank_specifier(p):
    """
    rank_specifier : L_BRACKET  dim_separators_opt  R_BRACKET  
    """
    pass


def p_dim_separators(p):
    """
    dim_separators : COMMA  
                   | dim_separators  COMMA  
    """
    pass


def p_delegate_type(p):
    """
    delegate_type : type_name  
    """
    pass


##################################################
# C.2.3 Variables




def p_variable_reference(p):
    """
    variable_reference : expression  
    """
    pass


##################################################
# C.2.4 Expressions


def p_argument_list(p):
    """
    argument_list : argument  
                  | argument_list  COMMA  argument  
    """
    pass


def p_argument(p):
    """
    argument : expression  
             | REF  variable_reference  
             | OUT  variable_reference  
    """
    pass


def p_primary_expression(p):
    """
    primary_expression : primary_no_array_creation_expression  
                       | array_creation_expression  
    """
    pass


def p_primary_no_array_creation_expression(p):
    """
    primary_no_array_creation_expression : literal  
                                         | simple_name  
                                         | parenthesized_expression  
                                         | member_access  
                                         | invocation_expression  
                                         | element_access  
                                         | this_access  
                                         | base_access  
                                         | post_increment_expression  
                                         | post_decrement_expression  
                                         | object_creation_expression  
                                         | delegate_creation_expression  
                                         | typeof_expression  
                                         | sizeof_expression  
                                         | checked_expression  
                                         | unchecked_expression  
    """
    pass


def p_simple_name(p):
    """
    simple_name : identifier  
    """
    pass


def p_parenthesized_expression(p):
    """
    parenthesized_expression : L_PAREN  expression  R_PAREN  
    """
    pass


def p_member_access(p):
    """
    member_access : primary_expression  PERIOD  identifier  
                  | predefined_type  PERIOD  identifier  
                  | predefined_type:  one  of  
                  | BOOL  BYTE  CHAR  DECIMAL  DOUBLE  FLOAT  INT  LONG  
                  | OBJECT  SBYTE  SHORT  STRING  UINT  ULONG  USHORT  
    """
    pass


def p_invocation_expression(p):
    """
    invocation_expression : primary_expression  L_PAREN  argument_list_opt  R_PAREN  
    """
    pass


def p_element_access(p):
    """
    element_access : primary_no_array_creation_expression  L_BRACKET  expression_list  R_BRACKET  
    """
    pass


def p_expression_list(p):
    """
    expression_list : expression  
                    | expression_list  COMMA  expression  
    """
    pass


def p_this_access(p):
    """
    this_access : THIS  
    """
    pass


def p_base_access(p):
    """
    base_access : BASE  PERIOD  identifier  
                | BASE  L_BRACKET  expression_list  R_BRACKET  
    """
    pass


def p_post_increment_expression(p):
    """
    post_increment_expression : primary_expression  PLUS_PLUS  
    """
    pass


def p_post_decrement_expression(p):
    """
    post_decrement_expression : primary_expression  MINUS_MINUS  
    """
    pass


def p_object_creation_expression(p):
    """
    object_creation_expression : NEW  type  L_PAREN  argument_list_opt  R_PAREN  
    """
    pass


def p_array_creation_expression(p):
    """
    array_creation_expression : NEW  non_array_type  L_BRACKET  expression_list  R_BRACKET  rank_specifiers_opt  array_initializer_opt  
                              | NEW  array_type  array_initializer  
    """
    pass


def p_delegate_creation_expression(p):
    """
    delegate_creation_expression : NEW  delegate_type  L_PAREN  expression  R_PAREN  
    """
    pass


def p_typeof_expression(p):
    """
    typeof_expression : TYPEOF  L_PAREN  type  R_PAREN  
                      | TYPEOF  L_PAREN  VOID  R_PAREN  
    """
    pass


def p_checked_expression(p):
    """
    checked_expression : CHECKED  L_PAREN  expression  R_PAREN  
    """
    pass


def p_unchecked_expression(p):
    """
    unchecked_expression : UNCHECKED  L_PAREN  expression  R_PAREN  
    """
    pass


def p_unary_expression(p):
    """
    unary_expression : primary_expression  
                     | PLUS  unary_expression  
                     | MINUS  unary_expression  
                     | L_NOT  unary_expression  
                     | NOT  unary_expression  
                     | TIMES  unary_expression  
                     | pre_increment_expression  
                     | pre_decrement_expression  
                     | cast_expression  
    """
    pass


def p_pre_increment_expression(p):
    """
    pre_increment_expression : PLUS_PLUS  unary_expression  
    """
    pass


def p_pre_decrement_expression(p):
    """
    pre_decrement_expression : MINUS_MINUS  unary_expression  
    """
    pass


def p_cast_expression(p):
    """
    cast_expression : L_PAREN  type  R_PAREN  unary_expression  
    """
    pass


def p_multiplicative_expression(p):
    """
    multiplicative_expression : unary_expression  
                              | multiplicative_expression  TIMES  unary_expression  
                              | multiplicative_expression  DIVIDE  unary_expression  
                              | multiplicative_expression  MOD  unary_expression  
    """
    pass


def p_additive_expression(p):
    """
    additive_expression : multiplicative_expression  
                        | additive_expression  PLUS  multiplicative_expression  
                        | additive_expression  –  multiplicative_expression  
    """
    pass


def p_shift_expression(p):
    """
    shift_expression : additive_expression  
                     | shift_expression  L_SHIFT  additive_expression  
                     | shift_expression  R_SHIFT  additive_expression  
    """
    pass


def p_relational_expression(p):
    """
    relational_expression : shift_expression  
                          | relational_expression  LT  shift_expression  
                          | relational_expression  GT  shift_expression  
                          | relational_expression  LE  shift_expression  
                          | relational_expression  GE  shift_expression  
                          | relational_expression  IS  type  
                          | relational_expression  AS  type  
    """
    pass


def p_equality_expression(p):
    """
    equality_expression : relational_expression  
                        | equality_expression  EQ  relational_expression  
                        | equality_expression  NE  relational_expression  
    """
    pass


def p_and_expression(p):
    """
    and_expression : equality_expression  
                   | and_expression  AND  equality_expression  
    """
    pass


def p_exclusive_or_expression(p):
    """
    exclusive_or_expression : and_expression  
                            | exclusive_or_expression  XOR  and_expression  
    """
    pass


def p_inclusive_or_expression(p):
    """
    inclusive_or_expression : exclusive_or_expression  
                            | inclusive_or_expression  OR  exclusive_or_expression  
    """
    pass


def p_conditional_and_expression(p):
    """
    conditional_and_expression : inclusive_or_expression  
                               | conditional_and_expression  L_AND  inclusive_or_expression  
    """
    pass


def p_conditional_or_expression(p):
    """
    conditional_or_expression : conditional_and_expression  
                              | conditional_or_expression  L_OR  conditional_and_expression  
    """
    pass


def p_conditional_expression(p):
    """
    conditional_expression : conditional_or_expression  
                           | conditional_or_expression  CONDOP  expression  COLON  expression  
    """
    pass


def p_assignment(p):
    """
    assignment : unary_expression  assignment_operator  expression  
               | assignment_operator:  one  of  
               | EQUALS  PLUS_EQUAL  MINUS_EQUAL  TIMES_EQUAL  DIV_EQUAL  MOD_EQUAL  AND_EQUAL  OR_EQUAL  XOR_EQUAL  L_SHIFT_EQUAL  R_SHIFT_EQUAL  
    """
    pass


def p_expression(p):
    """
    expression : conditional_expression  
               | assignment  
    """
    pass


def p_constant_expression(p):
    """
    constant_expression : expression  
    """
    pass


def p_boolean_expression(p):
    """
    boolean_expression : expression  
    """
    pass


##################################################
# C.2.5 Statements

def p_statement(p):
    """
    statement : labeled_statement  
              | declaration_statement  
              | embedded_statement  
    """
    pass


def p_embedded_statement(p):
    """
    embedded_statement : block  
                       | empty_statement  
                       | expression_statement  
                       | selection_statement  
                       | iteration_statement  
                       | jump_statement  
                       | try_statement  
                       | checked_statement  
                       | unchecked_statement  
                       | lock_statement  
                       | using_statement  
    """
    pass


def p_block(p):
    """
    block : L_BRACE  statement_list_opt  R_BRACE  
    """
    pass


def p_statement_list(p):
    """
    statement_list : statement  
                   | statement_list  statement  
    """
    pass


def p_empty_statement(p):
    """
    empty_statement : SEMI  
    """
    pass


def p_labeled_statement(p):
    """
    labeled_statement : identifier  COLON  statement  
    """
    pass


def p_declaration_statement(p):
    """
    declaration_statement : local_variable_declaration  SEMI  
                          | local_constant_declaration  SEMI  
    """
    pass


def p_local_variable_declaration(p):
    """
    local_variable_declaration : type  local_variable_declarators  
    """
    pass


def p_local_variable_declarators(p):
    """
    local_variable_declarators : local_variable_declarator  
                               | local_variable_declarators  COMMA  local_variable_declarator  
    """
    pass


def p_local_variable_declarator(p):
    """
    local_variable_declarator : identifier  
                              | identifier  EQUALS  local_variable_initializer  
    """
    pass


def p_local_variable_initializer(p):
    """
    local_variable_initializer : expression  
                               | array_initializer  
    """
    pass


def p_local_constant_declaration(p):
    """
    local_constant_declaration : CONST  type  constant_declarators  
    """
    pass


def p_constant_declarators(p):
    """
    constant_declarators : constant_declarator  
                         | constant_declarators  COMMA  constant_declarator  
    """
    pass


def p_constant_declarator(p):
    """
    constant_declarator : identifier  EQUALS  constant_expression  
    """
    pass


def p_expression_statement(p):
    """
    expression_statement : statement_expression  SEMI  
    """
    pass


def p_statement_expression(p):
    """
    statement_expression : invocation_expression  
                         | object_creation_expression  
                         | assignment  
                         | post_increment_expression  
                         | post_decrement_expression  
                         | pre_increment_expression  
                         | pre_decrement_expression  
    """
    pass


def p_selection_statement(p):
    """
    selection_statement : if_statement  
                        | switch_statement  
    """
    pass


def p_if_statement(p):
    """
    if_statement : IF  L_PAREN  boolean_expression  R_PAREN  embedded_statement  
                 | IF  L_PAREN  boolean_expression  R_PAREN  embedded_statement  ELSE  embedded_statement  
    """
    pass


def p_boolean_expression(p):
    """
    boolean_expression : expression  
    """
    pass


def p_switch_statement(p):
    """
    switch_statement : SWITCH  L_PAREN  expression  R_PAREN  switch_block  
    """
    pass


def p_switch_block(p):
    """
    switch_block : L_BRACE  switch_sections_opt  R_BRACE  
    """
    pass


def p_switch_sections(p):
    """
    switch_sections : switch_section  
                    | switch_sections  switch_section  
    """
    pass


def p_switch_section(p):
    """
    switch_section : switch_labels  statement_list  
    """
    pass


def p_switch_labels(p):
    """
    switch_labels : switch_label  
                  | switch_labels  switch_label  
    """
    pass


def p_switch_label(p):
    """
    switch_label : CASE  constant_expression  COLON  
                 | DEFAULT  COLON  
    """
    pass


def p_iteration_statement(p):
    """
    iteration_statement : while_statement  
                        | do_statement  
                        | for_statement  
                        | foreach_statement  
    """
    pass


def p_while_statement(p):
    """
    while_statement : WHILE  L_PAREN  boolean_expression  R_PAREN  embedded_statement  
    """
    pass


def p_do_statement(p):
    """
    do_statement : DO  embedded_statement  WHILE  L_PAREN  boolean_expression  R_PAREN  SEMI  
    """
    pass


def p_for_statement(p):
    """
    for_statement : FOR  L_PAREN  for_initializer_opt  SEMI  for_condition_opt  SEMI  for_iterator_opt  R_PAREN  embedded_statement  
    """
    pass


def p_for_initializer(p):
    """
    for_initializer : local_variable_declaration  
                    | statement_expression_list  
    """
    pass


def p_for_condition(p):
    """
    for_condition : boolean_expression  
    """
    pass


def p_for_iterator(p):
    """
    for_iterator : statement_expression_list  
    """
    pass


def p_statement_expression_list(p):
    """
    statement_expression_list : statement_expression  
                              | statement_expression_list  COMMA  statement_expression  
    """
    pass


def p_foreach_statement(p):
    """
    foreach_statement : FOREACH  L_PAREN  type  identifier  IN  expression  R_PAREN  embedded_statement  
    """
    pass


def p_jump_statement(p):
    """
    jump_statement : break_statement  
                   | continue_statement  
                   | goto_statement  
                   | return_statement  
                   | throw_statement  
    """
    pass


def p_break_statement(p):
    """
    break_statement : BREAK  SEMI  
    """
    pass


def p_continue_statement(p):
    """
    continue_statement : CONTINUE  SEMI  
    """
    pass


def p_goto_statement(p):
    """
    goto_statement : GOTO  identifier  SEMI  
                   | GOTO  CASE  constant_expression  SEMI  
                   | GOTO  DEFAULT  SEMI  
    """
    pass


def p_return_statement(p):
    """
    return_statement : RETURN  expression_opt  SEMI  
    """
    pass


def p_throw_statement(p):
    """
    throw_statement : THROW  expression_opt  SEMI  
    """
    pass


def p_try_statement(p):
    """
    try_statement : TRY  block  catch_clauses  
                  | TRY  block  finally_clause  
                  | TRY  block  catch_clauses  finally_clause  
    """
    pass


def p_catch_clauses(p):
    """
    catch_clauses : specific_catch_clauses  general_catch_clause_opt  
                  | specific_catch_clauses_opt  general_catch_clause  
    """
    pass


def p_specific_catch_clauses(p):
    """
    specific_catch_clauses : specific_catch_clause  
                           | specific_catch_clauses  specific_catch_clause  
    """
    pass


def p_specific_catch_clause(p):
    """
    specific_catch_clause : CATCH  L_PAREN  class_type  identifier_opt  R_PAREN  block  
    """
    pass


def p_general_catch_clause(p):
    """
    general_catch_clause : CATCH  block  
    """
    pass


def p_finally_clause(p):
    """
    finally_clause : FINALLY  block  
    """
    pass


def p_checked_statement(p):
    """
    checked_statement : CHECKED  block  
    """
    pass


def p_unchecked_statement(p):
    """
    unchecked_statement : UNCHECKED  block  
    """
    pass


def p_lock_statement(p):
    """
    lock_statement : LOCK  L_PAREN  expression  R_PAREN  embedded_statement  
    """
    pass


def p_using_statement(p):
    """
    using_statement : USING  L_PAREN  resource_acquisition  R_PAREN  embedded_statement  
    """
    pass


def p_resource_acquisition(p):
    """
    resource_acquisition : local_variable_declaration  
                         | expression  
    """
    pass


##################################################
# C.2.6 Namespaces

def p_compilation_unit(p):
    """
    compilation_unit : using_directives_opt  global_attributes_opt  namespace_member_declarations_opt  
    """
    pass


def p_namespace_declaration(p):
    """
    namespace_declaration : NAMESPACE  qualified_identifier  namespace_body  ;opt  
    """
    pass


def p_qualified_identifier(p):
    """
    qualified_identifier : identifier  
                         | qualified_identifier  PERIOD  identifier  
    """
    pass


def p_namespace_body(p):
    """
    namespace_body : L_BRACE  using_directives_opt  namespace_member_declarations_opt  R_BRACE  
    """
    pass


def p_using_directives(p):
    """
    using_directives : using_directive  
                     | using_directives  using_directive  
    """
    pass


def p_using_directive(p):
    """
    using_directive : using_alias_directive  
                    | using_namespace_directive  
    """
    pass


def p_using_alias_directive(p):
    """
    using_alias_directive : USING  identifier  EQUALS  namespace_or_type_name  SEMI  
    """
    pass


def p_using_namespace_directive(p):
    """
    using_namespace_directive : USING  namespace_name  SEMI  
    """
    pass


def p_namespace_member_declarations(p):
    """
    namespace_member_declarations : namespace_member_declaration  
                                  | namespace_member_declarations  namespace_member_declaration  
    """
    pass


def p_namespace_member_declaration(p):
    """
    namespace_member_declaration : namespace_declaration  
                                 | type_declaration  
    """
    pass


def p_type_declaration(p):
    """
    type_declaration : class_declaration  
                     | struct_declaration  
                     | interface_declaration  
                     | enum_declaration  
                     | delegate_declaration  
    """
    pass


##################################################
# C.2.7 Classes


def p_class_declaration(p):
    """
    class_declaration : attributes_opt  class_modifiers_opt  CLASS  identifier  class_base_opt  class_body  ;opt  
    """
    pass


def p_class_modifiers(p):
    """
    class_modifiers : class_modifier  
                    | class_modifiers  class_modifier  
    """
    pass


def p_class_modifier(p):
    """
    class_modifier : NEW  
                   | PUBLIC  
                   | PROTECTED  
                   | INTERNAL  
                   | PRIVATE  
                   | ABSTRACT  
                   | SEALED  
    """
    pass


def p_class_base(p):
    """
    class_base : COLON  class_type  
               | COLON  interface_type_list  
               | COLON  class_type  COMMA  interface_type_list  
    """
    pass


def p_interface_type_list(p):
    """
    interface_type_list : interface_type  
                        | interface_type_list  COMMA  interface_type  
    """
    pass


def p_class_body(p):
    """
    class_body : L_BRACE  class_member_declarations_opt  R_BRACE  
    """
    pass


def p_class_member_declarations(p):
    """
    class_member_declarations : class_member_declaration  
                              | class_member_declarations  class_member_declaration  
    """
    pass


def p_class_member_declaration(p):
    """
    class_member_declaration : constant_declaration  
                             | field_declaration  
                             | method_declaration  
                             | property_declaration  
                             | event_declaration  
                             | indexer_declaration  
                             | operator_declaration  
                             | constructor_declaration  
                             | destructor_declaration  
                             | static_constructor_declaration  
                             | type_declaration  
    """
    pass


def p_constant_declaration(p):
    """
    constant_declaration : attributes_opt  constant_modifiers_opt  CONST  type  constant_declarators  SEMI  
    """
    pass


def p_constant_modifiers(p):
    """
    constant_modifiers : constant_modifier  
                       | constant_modifiers  constant_modifier  
    """
    pass


def p_constant_modifier(p):
    """
    constant_modifier : NEW  
                      | PUBLIC  
                      | PROTECTED  
                      | INTERNAL  
                      | PRIVATE  
    """
    pass


def p_constant_declarators(p):
    """
    constant_declarators : constant_declarator  
                         | constant_declarators  COMMA  constant_declarator  
    """
    pass


def p_constant_declarator(p):
    """
    constant_declarator : identifier  EQUALS  constant_expression  
    """
    pass


def p_field_declaration(p):
    """
    field_declaration : attributes_opt  field_modifiers_opt  type  variable_declarators  SEMI  
    """
    pass


def p_field_modifiers(p):
    """
    field_modifiers : field_modifier  
                    | field_modifiers  field_modifier  
    """
    pass


def p_field_modifier(p):
    """
    field_modifier : NEW  
                   | PUBLIC  
                   | PROTECTED  
                   | INTERNAL  
                   | PRIVATE  
                   | STATIC  
                   | READONLY  
                   | VOLATILE  
    """
    pass


def p_variable_declarators(p):
    """
    variable_declarators : variable_declarator  
                         | variable_declarators  COMMA  variable_declarator  
    """
    pass


def p_variable_declarator(p):
    """
    variable_declarator : identifier  
                        | identifier  EQUALS  variable_initializer  
    """
    pass


def p_variable_initializer(p):
    """
    variable_initializer : expression  
                         | array_initializer  
    """
    pass


def p_method_declaration(p):
    """
    method_declaration : method_header  method_body  
    """
    pass


def p_method_header(p):
    """
    method_header : attributes_opt  method_modifiers_opt  return_type  member_name  L_PAREN  formal_parameter_list_opt  R_PAREN  
    """
    pass


def p_method_modifiers(p):
    """
    method_modifiers : method_modifier  
                     | method_modifiers  method_modifier  
    """
    pass


def p_method_modifier(p):
    """
    method_modifier : NEW  
                    | PUBLIC  
                    | PROTECTED  
                    | INTERNAL  
                    | PRIVATE  
                    | STATIC  
                    | VIRTUAL  
                    | SEALED  
                    | OVERRIDE  
                    | ABSTRACT  
                    | EXTERN  
    """
    pass


def p_return_type(p):
    """
    return_type : type  
                | VOID  
    """
    pass


def p_member_name(p):
    """
    member_name : identifier  
                | interface_type  PERIOD  identifier  
    """
    pass


def p_method_body(p):
    """
    method_body : block  
                | SEMI  
    """
    pass


def p_formal_parameter_list(p):
    """
    formal_parameter_list : fixed_parameters  
                          | fixed_parameters  COMMA  parameter_array  
                          | parameter_array  
    """
    pass


def p_fixed_parameters(p):
    """
    fixed_parameters : fixed_parameter  
                     | fixed_parameters  COMMA  fixed_parameter  
    """
    pass


def p_fixed_parameter(p):
    """
    fixed_parameter : attributes_opt  parameter_modifier_opt  type  identifier  
    """
    pass


def p_parameter_modifier(p):
    """
    parameter_modifier : REF  
                       | OUT  
    """
    pass


def p_parameter_array(p):
    """
    parameter_array : attributes_opt  PARAMS  array_type  identifier  
    """
    pass


def p_property_declaration(p):
    """
    property_declaration : attributes_opt  property_modifiers_opt  type  member_name  L_BRACE  accessor_declarations  R_BRACE  
    """
    pass


def p_property_modifiers(p):
    """
    property_modifiers : property_modifier  
                       | property_modifiers  property_modifier  
    """
    pass


def p_property_modifier(p):
    """
    property_modifier : NEW  
                      | PUBLIC  
                      | PROTECTED  
                      | INTERNAL  
                      | PRIVATE  
                      | STATIC  
                      | VIRTUAL  
                      | SEALED  
                      | OVERRIDE  
                      | ABSTRACT  
                      | EXTERN  
    """
    pass


def p_member_name(p):
    """
    member_name : identifier  
                | interface_type  PERIOD  identifier  
    """
    pass


def p_accessor_declarations(p):
    """
    accessor_declarations : get_accessor_declaration  set_accessor_declaration_opt  
                          | set_accessor_declaration  get_accessor_declaration_opt  
    """
    pass


def p_get_accessor_declaration(p):
    """
    get_accessor_declaration : attributes_opt  get  accessor_body  
    """
    pass


def p_set_accessor_declaration(p):
    """
    set_accessor_declaration : attributes_opt  set  accessor_body  
    """
    pass


def p_accessor_body(p):
    """
    accessor_body : block  
                  | SEMI  
    """
    pass


def p_event_declaration(p):
    """
    event_declaration : attributes_opt  event_modifiers_opt  EVENT  type  variable_declarators  SEMI  
                      | attributes_opt  event_modifiers_opt  EVENT  type  member_name  L_BRACE  event_accessor_declarations  R_BRACE  
    """
    pass


def p_event_modifiers(p):
    """
    event_modifiers : event_modifier  
                    | event_modifiers  event_modifier  
    """
    pass


def p_event_modifier(p):
    """
    event_modifier : NEW  
                   | PUBLIC  
                   | PROTECTED  
                   | INTERNAL  
                   | PRIVATE  
                   | STATIC  
                   | VIRTUAL  
                   | SEALED  
                   | OVERRIDE  
                   | ABSTRACT  
                   | EXTERN  
    """
    pass


def p_event_accessor_declarations(p):
    """
    event_accessor_declarations : add_accessor_declaration  remove_accessor_declaration  
                                | remove_accessor_declaration  add_accessor_declaration  
    """
    pass


def p_add_accessor_declaration(p):
    """
    add_accessor_declaration : attributes_opt  add  block  
    """
    pass


def p_remove_accessor_declaration(p):
    """
    remove_accessor_declaration : attributes_opt  remove  block  
    """
    pass


def p_indexer_declaration(p):
    """
    indexer_declaration : attributes_opt  indexer_modifiers_opt  indexer_declarator  L_BRACE  accessor_declarations  R_BRACE  
    """
    pass


def p_indexer_modifiers(p):
    """
    indexer_modifiers : indexer_modifier  
                      | indexer_modifiers  indexer_modifier  
    """
    pass


def p_indexer_modifier(p):
    """
    indexer_modifier : NEW  
                     | PUBLIC  
                     | PROTECTED  
                     | INTERNAL  
                     | PRIVATE  
                     | VIRTUAL  
                     | SEALED  
                     | OVERRIDE  
                     | ABSTRACT  
                     | EXTERN  
    """
    pass


def p_indexer_declarator(p):
    """
    indexer_declarator : type  THIS  L_BRACKET  formal_parameter_list  R_BRACKET  
                       | type  interface_type  PERIOD  THIS  L_BRACKET  formal_parameter_list  R_BRACKET  
    """
    pass


def p_operator_declaration(p):
    """
    operator_declaration : attributes_opt  operator_modifiers  operator_declarator  operator_body  
    """
    pass


def p_operator_modifiers(p):
    """
    operator_modifiers : operator_modifier  
                       | operator_modifiers  operator_modifier  
    """
    pass


def p_operator_modifier(p):
    """
    operator_modifier : PUBLIC  
                      | STATIC  
                      | EXTERN  
    """
    pass


def p_operator_declarator(p):
    """
    operator_declarator : unary_operator_declarator  
                        | binary_operator_declarator  
                        | conversion_operator_declarator  
    """
    pass


def p_unary_operator_declarator(p):
    """
    unary_operator_declarator : type  OPERATOR  overloadable_unary_operator  L_PAREN  type  identifier  R_PAREN  
                              | overloadable_unary_operator:  one  of  
                              | PLUS  MINUS  L_NOT  NOT  PLUS_PLUS  MINUS_MINUS  TRUE  FALSE  
    """
    pass


def p_binary_operator_declarator(p):
    """
    binary_operator_declarator : type  OPERATOR  overloadable_binary_operator  L_PAREN  type  identifier  COMMA  type  identifier  R_PAREN  
                               | overloadable_binary_operator:  one  of  
                               | PLUS  MINUS  TIMES  DIVIDE  MOD  AND  OR  XOR  L_SHIFT  R_SHIFT  EQ  NE  GT  LT  GE  LE  
    """
    pass


def p_conversion_operator_declarator(p):
    """
    conversion_operator_declarator : IMPLICIT  OPERATOR  type  L_PAREN  type  identifier  R_PAREN  
                                   | EXPLICIT  OPERATOR  type  L_PAREN  type  identifier  R_PAREN  
    """
    pass


def p_operator_body(p):
    """
    operator_body : block  
                  | SEMI  
    """
    pass


def p_constructor_declaration(p):
    """
    constructor_declaration : attributes_opt  constructor_modifiers_opt  constructor_declarator  constructor_body  
    """
    pass


def p_constructor_modifiers(p):
    """
    constructor_modifiers : constructor_modifier  
                          | constructor_modifiers  constructor_modifier  
    """
    pass


def p_constructor_modifier(p):
    """
    constructor_modifier : PUBLIC  
                         | PROTECTED  
                         | INTERNAL  
                         | PRIVATE  
                         | EXTERN  
    """
    pass


def p_constructor_declarator(p):
    """
    constructor_declarator : identifier  L_PAREN  formal_parameter_list_opt  R_PAREN  constructor_initializer_opt  
    """
    pass


def p_constructor_initializer(p):
    """
    constructor_initializer : COLON  BASE  L_PAREN  argument_list_opt  R_PAREN  
                            | COLON  THIS  L_PAREN  argument_list_opt  R_PAREN  
    """
    pass


def p_constructor_body(p):
    """
    constructor_body : block  
                     | SEMI  
    """
    pass


def p_static_constructor_declaration(p):
    """
    static_constructor_declaration : attributes_opt  static_constructor_modifiers  identifier  L_PAREN  R_PAREN  static_constructor_body  
                                   | static_constructor_modifiers  
                                   | extern_opt  STATIC  
                                   | STATIC  extern_opt  
    """
    pass


def p_static_constructor_body(p):
    """
    static_constructor_body : block  
                            | SEMI  
    """
    pass


def p_destructor_declaration(p):
    """
    destructor_declaration : attributes_opt  extern_opt  NOT  identifier  L_PAREN  R_PAREN  destructor_body  
    """
    pass


def p_destructor_body(p):
    """
    destructor_body : block  
                    | SEMI  
    """
    pass


##################################################
# C.2.8 Structs

def p_struct_declaration(p):
    """
    struct_declaration : attributes_opt  struct_modifiers_opt  STRUCT  identifier  struct_interfaces_opt  struct_body  ;opt  
    """
    pass


def p_struct_modifiers(p):
    """
    struct_modifiers : struct_modifier  
                     | struct_modifiers  struct_modifier  
    """
    pass


def p_struct_modifier(p):
    """
    struct_modifier : NEW  
                    | PUBLIC  
                    | PROTECTED  
                    | INTERNAL  
                    | PRIVATE  
    """
    pass


def p_struct_interfaces(p):
    """
    struct_interfaces : COLON  interface_type_list  
    """
    pass


def p_struct_body(p):
    """
    struct_body : L_BRACE  struct_member_declarations_opt  R_BRACE  
    """
    pass


def p_struct_member_declarations(p):
    """
    struct_member_declarations : struct_member_declaration  
                               | struct_member_declarations  struct_member_declaration  
    """
    pass


def p_struct_member_declaration(p):
    """
    struct_member_declaration : constant_declaration  
                              | field_declaration  
                              | method_declaration  
                              | property_declaration  
                              | event_declaration  
                              | indexer_declaration  
                              | operator_declaration  
                              | constructor_declaration  
                              | static_constructor_declaration  
                              | type_declaration  
    """
    pass


##################################################
# C.2.9 Arrays


def p_array_type(p):
    """
    array_type : non_array_type  rank_specifiers  
    """
    pass


def p_non_array_type(p):
    """
    non_array_type : type  
    """
    pass


def p_rank_specifiers(p):
    """
    rank_specifiers : rank_specifier  
                    | rank_specifiers  rank_specifier  
    """
    pass


def p_rank_specifier(p):
    """
    rank_specifier : L_BRACKET  dim_separators_opt  R_BRACKET  
    """
    pass


def p_dim_separators(p):
    """
    dim_separators : COMMA  
                   | dim_separators  COMMA  
    """
    pass


def p_array_initializer(p):
    """
    array_initializer : L_BRACE  variable_initializer_list_opt  R_BRACE  
                      | L_BRACE  variable_initializer_list  COMMA  R_BRACE  
    """
    pass


def p_variable_initializer_list(p):
    """
    variable_initializer_list : variable_initializer  
                              | variable_initializer_list  COMMA  variable_initializer  
    """
    pass


def p_variable_initializer(p):
    """
    variable_initializer : expression  
                         | array_initializer  
    """
    pass


##################################################
# C.2.10 Interfaces


def p_interface_declaration(p):
    """
    interface_declaration : attributes_opt  interface_modifiers_opt  INTERFACE  identifier  interface_base_opt  interface_body  ;opt  
    """
    pass


def p_interface_modifiers(p):
    """
    interface_modifiers : interface_modifier  
                        | interface_modifiers  interface_modifier  
    """
    pass


def p_interface_modifier(p):
    """
    interface_modifier : NEW  
                       | PUBLIC  
                       | PROTECTED  
                       | INTERNAL  
                       | PRIVATE  
    """
    pass


def p_interface_base(p):
    """
    interface_base : COLON  interface_type_list  
    """
    pass


def p_interface_body(p):
    """
    interface_body : L_BRACE  interface_member_declarations_opt  R_BRACE  
    """
    pass


def p_interface_member_declarations(p):
    """
    interface_member_declarations : interface_member_declaration  
                                  | interface_member_declarations  interface_member_declaration  
    """
    pass


def p_interface_member_declaration(p):
    """
    interface_member_declaration : interface_method_declaration  
                                 | interface_property_declaration  
                                 | interface_event_declaration  
                                 | interface_indexer_declaration  
    """
    pass


def p_interface_method_declaration(p):
    """
    interface_method_declaration : attributes_opt  new_opt  return_type  identifier  L_PAREN  formal_parameter_list_opt  R_PAREN  SEMI  
    """
    pass


def p_interface_property_declaration(p):
    """
    interface_property_declaration : attributes_opt  new_opt  type  identifier  L_BRACE  interface_accessors  R_BRACE  
    """
    pass


def p_interface_accessors(p):
    """
    interface_accessors : attributes_opt  get  SEMI  
                        | attributes_opt  set  SEMI  
                        | attributes_opt  get  SEMI  attributes_opt  set  SEMI  
                        | attributes_opt  set  SEMI  attributes_opt  get  SEMI  
    """
    pass


def p_interface_event_declaration(p):
    """
    interface_event_declaration : attributes_opt  new_opt  EVENT  type  identifier  SEMI  
    """
    pass


def p_interface_indexer_declaration(p):
    """
    interface_indexer_declaration : attributes_opt  new_opt  type  THIS  L_BRACKET  formal_parameter_list  R_BRACKET  L_BRACE  interface_accessors  R_BRACE  
    """
    pass


##################################################
# C.2.11 Enums


def p_enum_declaration(p):
    """
    enum_declaration : attributes_opt  enum_modifiers_opt  ENUM  identifier  enum_base_opt  enum_body  ;opt  
    """
    pass


def p_enum_base(p):
    """
    enum_base : COLON  integral_type  
    """
    pass


def p_enum_body(p):
    """
    enum_body : L_BRACE  enum_member_declarations_opt  R_BRACE  
              | L_BRACE  enum_member_declarations  COMMA  R_BRACE  
    """
    pass


def p_enum_modifiers(p):
    """
    enum_modifiers : enum_modifier  
                   | enum_modifiers  enum_modifier  
    """
    pass


def p_enum_modifier(p):
    """
    enum_modifier : NEW  
                  | PUBLIC  
                  | PROTECTED  
                  | INTERNAL  
                  | PRIVATE  
    """
    pass


def p_enum_member_declarations(p):
    """
    enum_member_declarations : enum_member_declaration  
                             | enum_member_declarations  COMMA  enum_member_declaration  
    """
    pass


def p_enum_member_declaration(p):
    """
    enum_member_declaration : attributes_opt  identifier  
                            | attributes_opt  identifier  EQUALS  constant_expression  
    """
    pass


##################################################
# C.2.12 Delegates

def p_delegate_declaration(p):
    """
    delegate_declaration : attributes_opt  delegate_modifiers_opt  DELEGATE  return_type  identifier  L_PAREN  formal_parameter_list_opt  R_PAREN  SEMI  
    """
    pass


def p_delegate_modifiers(p):
    """
    delegate_modifiers : delegate_modifier  
                       | delegate_modifiers  delegate_modifier  
    """
    pass


def p_delegate_modifier(p):
    """
    delegate_modifier : NEW  
                      | PUBLIC  
                      | PROTECTED  
                      | INTERNAL  
                      | PRIVATE  
    """
    pass


##################################################
# C.2.13 Attributes


def p_global_attributes(p):
    """
    global_attributes : global_attribute_sections  
    """
    pass


def p_global_attribute_sections(p):
    """
    global_attribute_sections : global_attribute_section  
                              | global_attribute_sections  global_attribute_section  
    """
    pass


def p_global_attribute_section(p):
    """
    global_attribute_section : L_BRACKET  global_attribute_target_specifier  attribute_list  R_BRACKET  
                             | L_BRACKET  global_attribute_target_specifier  attribute_list  ,]  
    """
    pass


def p_global_attribute_target_specifier(p):
    """
    global_attribute_target_specifier : global_attribute_target  COLON  
    """
    pass


def p_global_attribute_target(p):
    """
    global_attribute_target : assembly  
                            | module  
    """
    pass


def p_attributes(p):
    """
    attributes : attribute_sections  
    """
    pass


def p_attribute_sections(p):
    """
    attribute_sections : attribute_section  
                       | attribute_sections  attribute_section  
    """
    pass


def p_attribute_section(p):
    """
    attribute_section : L_BRACKET  attribute_target_specifier_opt  attribute_list  R_BRACKET  
                      | L_BRACKET  attribute_target_specifier_opt  attribute_list  COMMA  R_BRACKET  
    """
    pass


def p_attribute_target_specifier(p):
    """
    attribute_target_specifier : attribute_target  COLON  
    """
    pass


def p_attribute_target(p):
    """
    attribute_target : field  
                     | EVENT  
                     | method  
                     | param  
                     | property  
                     | RETURN  
                     | type  
    """
    pass


def p_attribute_list(p):
    """
    attribute_list : attribute  
                   | attribute_list  COMMA  attribute  
    """
    pass


def p_attribute(p):
    """
    attribute : attribute_name  attribute_arguments_opt  
    """
    pass


def p_attribute_name(p):
    """
    attribute_name : type_name  
    """
    pass


def p_attribute_arguments(p):
    """
    attribute_arguments : L_PAREN  positional_argument_list_opt  R_PAREN  
                        | L_PAREN  positional_argument_list  COMMA  named_argument_list  R_PAREN  
                        | L_PAREN  named_argument_list  R_PAREN  
    """
    pass


def p_positional_argument_list(p):
    """
    positional_argument_list : positional_argument  
                             | positional_argument_list  COMMA  positional_argument  
    """
    pass


def p_positional_argument(p):
    """
    positional_argument : attribute_argument_expression  
    """
    pass


def p_named_argument_list(p):
    """
    named_argument_list : named_argument  
                        | named_argument_list  COMMA  named_argument  
    """
    pass


def p_named_argument(p):
    """
    named_argument : identifier  EQUALS  attribute_argument_expression  
    """
    pass


def p_attribute_argument_expression(p):
    """
    attribute_argument_expression : expression  
    """
    pass


##################################################
# C.2.31 Opt

def p_dim_separators_opt(p):
    """
    dim_separators_opt : dim_separators  
                       | empty  
    """
    pass


def p_argument_list_opt(p):
    """
    argument_list_opt : argument_list  
                      | empty  
    """
    pass


def p_argument_list_opt(p):
    """
    argument_list_opt : argument_list  
                      | empty  
    """
    pass


def p_rank_specifiers_opt(p):
    """
    rank_specifiers_opt : rank_specifiers  
                        | empty  
    """
    pass


def p_array_initializer_opt(p):
    """
    array_initializer_opt : array_initializer  
                          | empty  
    """
    pass


def p_statement_list_opt(p):
    """
    statement_list_opt : statement_list  
                       | empty  
    """
    pass


def p_switch_sections_opt(p):
    """
    switch_sections_opt : switch_sections  
                        | empty  
    """
    pass


def p_for_initializer_opt(p):
    """
    for_initializer_opt : for_initializer  
                        | empty  
    """
    pass


def p_for_condition_opt(p):
    """
    for_condition_opt : for_condition  
                      | empty  
    """
    pass


def p_for_iterator_opt(p):
    """
    for_iterator_opt : for_iterator  
                     | empty  
    """
    pass


def p_expression_opt(p):
    """
    expression_opt : expression  
                   | empty  
    """
    pass


def p_expression_opt(p):
    """
    expression_opt : expression  
                   | empty  
    """
    pass


def p_general_catch_clause_opt(p):
    """
    general_catch_clause_opt : general_catch_clause  
                             | empty  
    """
    pass


def p_specific_catch_clauses_opt(p):
    """
    specific_catch_clauses_opt : specific_catch_clauses  
                               | empty  
    """
    pass


def p_identifier_opt(p):
    """
    identifier_opt : identifier  
                   | empty  
    """
    pass


def p_using_directives_opt(p):
    """
    using_directives_opt : using_directives  
                         | empty  
    """
    pass


def p_global_attributes_opt(p):
    """
    global_attributes_opt : global_attributes  
                          | empty  
    """
    pass


def p_namespace_member_declarations_opt(p):
    """
    namespace_member_declarations_opt : namespace_member_declarations  
                                      | empty  
    """
    pass


def p_using_directives_opt(p):
    """
    using_directives_opt : using_directives  
                         | empty  
    """
    pass


def p_namespace_member_declarations_opt(p):
    """
    namespace_member_declarations_opt : namespace_member_declarations  
                                      | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_class_modifiers_opt(p):
    """
    class_modifiers_opt : class_modifiers  
                        | empty  
    """
    pass


def p_class_base_opt(p):
    """
    class_base_opt : class_base  
                   | empty  
    """
    pass


def p_class_member_declarations_opt(p):
    """
    class_member_declarations_opt : class_member_declarations  
                                  | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_constant_modifiers_opt(p):
    """
    constant_modifiers_opt : constant_modifiers  
                           | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_field_modifiers_opt(p):
    """
    field_modifiers_opt : field_modifiers  
                        | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_method_modifiers_opt(p):
    """
    method_modifiers_opt : method_modifiers  
                         | empty  
    """
    pass


def p_formal_parameter_list_opt(p):
    """
    formal_parameter_list_opt : formal_parameter_list  
                              | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_parameter_modifier_opt(p):
    """
    parameter_modifier_opt : parameter_modifier  
                           | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_property_modifiers_opt(p):
    """
    property_modifiers_opt : property_modifiers  
                           | empty  
    """
    pass


def p_set_accessor_declaration_opt(p):
    """
    set_accessor_declaration_opt : set_accessor_declaration  
                                 | empty  
    """
    pass


def p_get_accessor_declaration_opt(p):
    """
    get_accessor_declaration_opt : get_accessor_declaration  
                                 | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_event_modifiers_opt(p):
    """
    event_modifiers_opt : event_modifiers  
                        | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_event_modifiers_opt(p):
    """
    event_modifiers_opt : event_modifiers  
                        | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_indexer_modifiers_opt(p):
    """
    indexer_modifiers_opt : indexer_modifiers  
                          | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_constructor_modifiers_opt(p):
    """
    constructor_modifiers_opt : constructor_modifiers  
                              | empty  
    """
    pass


def p_formal_parameter_list_opt(p):
    """
    formal_parameter_list_opt : formal_parameter_list  
                              | empty  
    """
    pass


def p_constructor_initializer_opt(p):
    """
    constructor_initializer_opt : constructor_initializer  
                                | empty  
    """
    pass


def p_argument_list_opt(p):
    """
    argument_list_opt : argument_list  
                      | empty  
    """
    pass


def p_argument_list_opt(p):
    """
    argument_list_opt : argument_list  
                      | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_extern_opt(p):
    """
    extern_opt : EXTERN  
               | empty  
    """
    pass


def p_extern_opt(p):
    """
    extern_opt : EXTERN  
               | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_extern_opt(p):
    """
    extern_opt : EXTERN  
               | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_struct_modifiers_opt(p):
    """
    struct_modifiers_opt : struct_modifiers  
                         | empty  
    """
    pass


def p_struct_interfaces_opt(p):
    """
    struct_interfaces_opt : struct_interfaces  
                          | empty  
    """
    pass


def p_struct_member_declarations_opt(p):
    """
    struct_member_declarations_opt : struct_member_declarations  
                                   | empty  
    """
    pass


def p_dim_separators_opt(p):
    """
    dim_separators_opt : dim_separators  
                       | empty  
    """
    pass


def p_variable_initializer_list_opt(p):
    """
    variable_initializer_list_opt : variable_initializer_list  
                                  | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_interface_modifiers_opt(p):
    """
    interface_modifiers_opt : interface_modifiers  
                            | empty  
    """
    pass


def p_interface_base_opt(p):
    """
    interface_base_opt : interface_base  
                       | empty  
    """
    pass


def p_interface_member_declarations_opt(p):
    """
    interface_member_declarations_opt : interface_member_declarations  
                                      | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_new_opt(p):
    """
    new_opt : NEW  
            | empty  
    """
    pass


def p_formal_parameter_list_opt(p):
    """
    formal_parameter_list_opt : formal_parameter_list  
                              | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_new_opt(p):
    """
    new_opt : NEW  
            | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_new_opt(p):
    """
    new_opt : NEW  
            | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_new_opt(p):
    """
    new_opt : NEW  
            | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_enum_modifiers_opt(p):
    """
    enum_modifiers_opt : enum_modifiers  
                       | empty  
    """
    pass


def p_enum_base_opt(p):
    """
    enum_base_opt : enum_base  
                  | empty  
    """
    pass


def p_enum_member_declarations_opt(p):
    """
    enum_member_declarations_opt : enum_member_declarations  
                                 | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_attributes_opt(p):
    """
    attributes_opt : attributes  
                   | empty  
    """
    pass


def p_delegate_modifiers_opt(p):
    """
    delegate_modifiers_opt : delegate_modifiers  
                           | empty  
    """
    pass


def p_formal_parameter_list_opt(p):
    """
    formal_parameter_list_opt : formal_parameter_list  
                              | empty  
    """
    pass


def p_attribute_target_specifier_opt(p):
    """
    attribute_target_specifier_opt : attribute_target_specifier  
                                   | empty  
    """
    pass


def p_attribute_target_specifier_opt(p):
    """
    attribute_target_specifier_opt : attribute_target_specifier  
                                   | empty  
    """
    pass


def p_attribute_arguments_opt(p):
    """
    attribute_arguments_opt : attribute_arguments  
                            | empty  
    """
    pass


def p_positional_argument_list_opt(p):
    """
    positional_argument_list_opt : positional_argument_list  
                                 | empty  
    """
    pass


def p_empty(p):
    """
    empty :   
    """
    pass
