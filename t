
##################################################
# C.2.1 Basic concepts

namespace-name: namespace-or-type-name  
type-name: namespace-or-type-name  
namespace-or-type-name: identifier  
                       | namespace-or-type-name  PERIOD  identifier  

##################################################
# C.2.2 Types

type: value-type  
     | reference-type  
value-type: struct-type  
           | enum-type  
struct-type: type-name  
            | simple-type  
simple-type: numeric-type  
            | BOOL  
numeric-type: integral-type  
             | floating-point-type  
             | DECIMAL  
integral-type: SBYTE  
              | BYTE  
              | SHORT  
              | USHORT  
              | INT  
              | UINT  
              | LONG  
              | ULONG  
              | CHAR  
floating-point-type: FLOAT  
                    | DOUBLE  
enum-type: type-name  
reference-type: class-type  
               | interface-type  
               | array-type  
               | delegate-type  
class-type: type-name  
           | OBJECT  
           | STRING  
interface-type: type-name  
array-type: non-array-type  rank-specifiers  
non-array-type: type  
rank-specifiers: rank-specifier  
                | rank-specifiers  rank-specifier  
rank-specifier: L_BRACKET  dim-separators-opt  R_BRACKET  
dim-separators: COMMA  
               | dim-separators  COMMA  
delegate-type: type-name  

##################################################
# C.2.3 Variables

variable-reference: expression  

##################################################
# C.2.4 Expressions

argument-list: argument  
              | argument-list  COMMA  argument  
argument: expression  
         | REF  variable-reference  
         | OUT  variable-reference  
primary-expression: primary-no-array-creation-expression  
                   | array-creation-expression  
primary-no-array-creation-expression: literal  
                                     | simple-name  
                                     | parenthesized-expression  
                                     | member-access  
                                     | invocation-expression  
                                     | element-access  
                                     | this-access  
                                     | base-access  
                                     | post-increment-expression  
                                     | post-decrement-expression  
                                     | object-creation-expression  
                                     | delegate-creation-expression  
                                     | typeof-expression  
                                     | sizeof-expression  
                                     | checked-expression  
                                     | unchecked-expression  
simple-name: identifier  
parenthesized-expression: L_PAREN  expression  R_PAREN  
member-access: primary-expression  PERIOD  identifier  
              | predefined-type  PERIOD  identifier  
              | predefined-type:  one  of  
              | BOOL  BYTE  CHAR  DECIMAL  DOUBLE  FLOAT  INT  LONG  
              | OBJECT  SBYTE  SHORT  STRING  UINT  ULONG  USHORT  
invocation-expression: primary-expression  L_PAREN  argument-list-opt  R_PAREN  
element-access: primary-no-array-creation-expression  L_BRACKET  expression-list  R_BRACKET  
expression-list: expression  
                | expression-list  COMMA  expression  
this-access: THIS  
base-access: BASE  PERIOD  identifier  
            | BASE  L_BRACKET  expression-list  R_BRACKET  
post-increment-expression: primary-expression  PLUS_PLUS  
post-decrement-expression: primary-expression  MINUS_MINUS  
object-creation-expression: NEW  type  L_PAREN  argument-list-opt  R_PAREN  
array-creation-expression: NEW  non-array-type  L_BRACKET  expression-list  R_BRACKET  rank-specifiers-opt  array-initializer-opt  
                          | NEW  array-type  array-initializer  
delegate-creation-expression: NEW  delegate-type  L_PAREN  expression  R_PAREN  
typeof-expression: TYPEOF  L_PAREN  type  R_PAREN  
                  | TYPEOF  L_PAREN  VOID  R_PAREN  
checked-expression: CHECKED  L_PAREN  expression  R_PAREN  
unchecked-expression: UNCHECKED  L_PAREN  expression  R_PAREN  
unary-expression: primary-expression  
                 | PLUS  unary-expression  
                 | MINUS  unary-expression  
                 | L_NOT  unary-expression  
                 | NOT  unary-expression  
                 | TIMES  unary-expression  
                 | pre-increment-expression  
                 | pre-decrement-expression  
                 | cast-expression  
pre-increment-expression: PLUS_PLUS  unary-expression  
pre-decrement-expression: MINUS_MINUS  unary-expression  
cast-expression: L_PAREN  type  R_PAREN  unary-expression  
multiplicative-expression: unary-expression  
                          | multiplicative-expression  TIMES  unary-expression  
                          | multiplicative-expression  DIVIDE  unary-expression  
                          | multiplicative-expression  MOD  unary-expression  
additive-expression: multiplicative-expression  
                    | additive-expression  PLUS  multiplicative-expression  
                    | additive-expression  –  multiplicative-expression  
shift-expression: additive-expression  
                 | shift-expression  L_SHIFT  additive-expression  
                 | shift-expression  R_SHIFT  additive-expression  
relational-expression: shift-expression  
                      | relational-expression  LT  shift-expression  
                      | relational-expression  GT  shift-expression  
                      | relational-expression  LE  shift-expression  
                      | relational-expression  GE  shift-expression  
                      | relational-expression  IS  type  
                      | relational-expression  AS  type  
equality-expression: relational-expression  
                    | equality-expression  EQ  relational-expression  
                    | equality-expression  NE  relational-expression  
and-expression: equality-expression  
               | and-expression  AND  equality-expression  
exclusive-or-expression: and-expression  
                        | exclusive-or-expression  XOR  and-expression  
inclusive-or-expression: exclusive-or-expression  
                        | inclusive-or-expression  OR  exclusive-or-expression  
conditional-and-expression: inclusive-or-expression  
                           | conditional-and-expression  L_AND  inclusive-or-expression  
conditional-or-expression: conditional-and-expression  
                          | conditional-or-expression  L_OR  conditional-and-expression  
conditional-expression: conditional-or-expression  
                       | conditional-or-expression  CONDOP  expression  COLON  expression  
assignment: unary-expression  assignment-operator  expression  
           | assignment-operator:  one  of  
           | EQUALS  PLUS_EQUAL  MINUS_EQUAL  TIMES_EQUAL  DIV_EQUAL  MOD_EQUAL  AND_EQUAL  OR_EQUAL  XOR_EQUAL  L_SHIFT_EQUAL  R_SHIFT_EQUAL  
expression: conditional-expression  
           | assignment  
constant-expression: expression  
boolean-expression: expression  

##################################################
# C.2.5 Statements

statement: labeled-statement  
          | declaration-statement  
          | embedded-statement  
embedded-statement: block  
                   | empty-statement  
                   | expression-statement  
                   | selection-statement  
                   | iteration-statement  
                   | jump-statement  
                   | try-statement  
                   | checked-statement  
                   | unchecked-statement  
                   | lock-statement  
                   | using-statement  
block: L_BRACE  statement-list-opt  R_BRACE  
statement-list: statement  
               | statement-list  statement  
empty-statement: SEMI  
labeled-statement: identifier  COLON  statement  
declaration-statement: local-variable-declaration  SEMI  
                      | local-constant-declaration  SEMI  
local-variable-declaration: type  local-variable-declarators  
local-variable-declarators: local-variable-declarator  
                           | local-variable-declarators  COMMA  local-variable-declarator  
local-variable-declarator: identifier  
                          | identifier  EQUALS  local-variable-initializer  
local-variable-initializer: expression  
                           | array-initializer  
local-constant-declaration: CONST  type  constant-declarators  
constant-declarators: constant-declarator  
                     | constant-declarators  COMMA  constant-declarator  
constant-declarator: identifier  EQUALS  constant-expression  
expression-statement: statement-expression  SEMI  
statement-expression: invocation-expression  
                     | object-creation-expression  
                     | assignment  
                     | post-increment-expression  
                     | post-decrement-expression  
                     | pre-increment-expression  
                     | pre-decrement-expression  
selection-statement: if-statement  
                    | switch-statement  
if-statement: IF  L_PAREN  boolean-expression  R_PAREN  embedded-statement  
             | IF  L_PAREN  boolean-expression  R_PAREN  embedded-statement  ELSE  embedded-statement  
boolean-expression: expression  
switch-statement: SWITCH  L_PAREN  expression  R_PAREN  switch-block  
switch-block: L_BRACE  switch-sections-opt  R_BRACE  
switch-sections: switch-section  
                | switch-sections  switch-section  
switch-section: switch-labels  statement-list  
switch-labels: switch-label  
              | switch-labels  switch-label  
switch-label: CASE  constant-expression  COLON  
             | DEFAULT  COLON  
iteration-statement: while-statement  
                    | do-statement  
                    | for-statement  
                    | foreach-statement  
while-statement: WHILE  L_PAREN  boolean-expression  R_PAREN  embedded-statement  
do-statement: DO  embedded-statement  WHILE  L_PAREN  boolean-expression  R_PAREN  SEMI  
for-statement: FOR  L_PAREN  for-initializer-opt  SEMI  for-condition-opt  SEMI  for-iterator-opt  R_PAREN  embedded-statement  
for-initializer: local-variable-declaration  
                | statement-expression-list  
for-condition: boolean-expression  
for-iterator: statement-expression-list  
statement-expression-list: statement-expression  
                          | statement-expression-list  COMMA  statement-expression  
foreach-statement: FOREACH  L_PAREN  type  identifier  IN  expression  R_PAREN  embedded-statement  
jump-statement: break-statement  
               | continue-statement  
               | goto-statement  
               | return-statement  
               | throw-statement  
break-statement: BREAK  SEMI  
continue-statement: CONTINUE  SEMI  
goto-statement: GOTO  identifier  SEMI  
               | GOTO  CASE  constant-expression  SEMI  
               | GOTO  DEFAULT  SEMI  
return-statement: RETURN  expression-opt  SEMI  
throw-statement: THROW  expression-opt  SEMI  
try-statement: TRY  block  catch-clauses  
              | TRY  block  finally-clause  
              | TRY  block  catch-clauses  finally-clause  
catch-clauses: specific-catch-clauses  general-catch-clause-opt  
              | specific-catch-clauses-opt  general-catch-clause  
specific-catch-clauses: specific-catch-clause  
                       | specific-catch-clauses  specific-catch-clause  
specific-catch-clause: CATCH  L_PAREN  class-type  identifier-opt  R_PAREN  block  
general-catch-clause: CATCH  block  
finally-clause: FINALLY  block  
checked-statement: CHECKED  block  
unchecked-statement: UNCHECKED  block  
lock-statement: LOCK  L_PAREN  expression  R_PAREN  embedded-statement  
using-statement: USING  L_PAREN  resource-acquisition  R_PAREN  embedded-statement  
resource-acquisition: local-variable-declaration  
                     | expression  

##################################################
# C.2.6 Namespaces

compilation-unit: using-directives-opt  global-attributes-opt  namespace-member-declarations-opt  
namespace-declaration: NAMESPACE  qualified-identifier  namespace-body  ;opt  
qualified-identifier: identifier  
                     | qualified-identifier  PERIOD  identifier  
namespace-body: L_BRACE  using-directives-opt  namespace-member-declarations-opt  R_BRACE  
using-directives: using-directive  
                 | using-directives  using-directive  
using-directive: using-alias-directive  
                | using-namespace-directive  
using-alias-directive: USING  identifier  EQUALS  namespace-or-type-name  SEMI  
using-namespace-directive: USING  namespace-name  SEMI  
namespace-member-declarations: namespace-member-declaration  
                              | namespace-member-declarations  namespace-member-declaration  
namespace-member-declaration: namespace-declaration  
                             | type-declaration  
type-declaration: class-declaration  
                 | struct-declaration  
                 | interface-declaration  
                 | enum-declaration  
                 | delegate-declaration  

##################################################
# C.2.7 Classes

class-declaration: attributes-opt  class-modifiers-opt  CLASS  identifier  class-base-opt  class-body  ;opt  
class-modifiers: class-modifier  
                | class-modifiers  class-modifier  
class-modifier: NEW  
               | PUBLIC  
               | PROTECTED  
               | INTERNAL  
               | PRIVATE  
               | ABSTRACT  
               | SEALED  
class-base: COLON  class-type  
           | COLON  interface-type-list  
           | COLON  class-type  COMMA  interface-type-list  
interface-type-list: interface-type  
                    | interface-type-list  COMMA  interface-type  
class-body: L_BRACE  class-member-declarations-opt  R_BRACE  
class-member-declarations: class-member-declaration  
                          | class-member-declarations  class-member-declaration  
class-member-declaration: constant-declaration  
                         | field-declaration  
                         | method-declaration  
                         | property-declaration  
                         | event-declaration  
                         | indexer-declaration  
                         | operator-declaration  
                         | constructor-declaration  
                         | destructor-declaration  
                         | static-constructor-declaration  
                         | type-declaration  
constant-declaration: attributes-opt  constant-modifiers-opt  CONST  type  constant-declarators  SEMI  
constant-modifiers: constant-modifier  
                   | constant-modifiers  constant-modifier  
constant-modifier: NEW  
                  | PUBLIC  
                  | PROTECTED  
                  | INTERNAL  
                  | PRIVATE  
constant-declarators: constant-declarator  
                     | constant-declarators  COMMA  constant-declarator  
constant-declarator: identifier  EQUALS  constant-expression  
field-declaration: attributes-opt  field-modifiers-opt  type  variable-declarators  SEMI  
field-modifiers: field-modifier  
                | field-modifiers  field-modifier  
field-modifier: NEW  
               | PUBLIC  
               | PROTECTED  
               | INTERNAL  
               | PRIVATE  
               | STATIC  
               | READONLY  
               | VOLATILE  
variable-declarators: variable-declarator  
                     | variable-declarators  COMMA  variable-declarator  
variable-declarator: identifier  
                    | identifier  EQUALS  variable-initializer  
variable-initializer: expression  
                     | array-initializer  
method-declaration: method-header  method-body  
method-header: attributes-opt  method-modifiers-opt  return-type  member-name  L_PAREN  formal-parameter-list-opt  R_PAREN  
method-modifiers: method-modifier  
                 | method-modifiers  method-modifier  
method-modifier: NEW  
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
return-type: type  
            | VOID  
member-name: identifier  
            | interface-type  PERIOD  identifier  
method-body: block  
            | SEMI  
formal-parameter-list: fixed-parameters  
                      | fixed-parameters  COMMA  parameter-array  
                      | parameter-array  
fixed-parameters: fixed-parameter  
                 | fixed-parameters  COMMA  fixed-parameter  
fixed-parameter: attributes-opt  parameter-modifier-opt  type  identifier  
parameter-modifier: REF  
                   | OUT  
parameter-array: attributes-opt  PARAMS  array-type  identifier  
property-declaration: attributes-opt  property-modifiers-opt  type  member-name  L_BRACE  accessor-declarations  R_BRACE  
property-modifiers: property-modifier  
                   | property-modifiers  property-modifier  
property-modifier: NEW  
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
member-name: identifier  
            | interface-type  PERIOD  identifier  
accessor-declarations: get-accessor-declaration  set-accessor-declaration-opt  
                      | set-accessor-declaration  get-accessor-declaration-opt  
get-accessor-declaration: attributes-opt  get  accessor-body  
set-accessor-declaration: attributes-opt  set  accessor-body  
accessor-body: block  
              | SEMI  
event-declaration: attributes-opt  event-modifiers-opt  EVENT  type  variable-declarators  SEMI  
                  | attributes-opt  event-modifiers-opt  EVENT  type  member-name  L_BRACE  event-accessor-declarations  R_BRACE  
event-modifiers: event-modifier  
                | event-modifiers  event-modifier  
event-modifier: NEW  
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
event-accessor-declarations: add-accessor-declaration  remove-accessor-declaration  
                            | remove-accessor-declaration  add-accessor-declaration  
add-accessor-declaration: attributes-opt  add  block  
remove-accessor-declaration: attributes-opt  remove  block  
indexer-declaration: attributes-opt  indexer-modifiers-opt  indexer-declarator  L_BRACE  accessor-declarations  R_BRACE  
indexer-modifiers: indexer-modifier  
                  | indexer-modifiers  indexer-modifier  
indexer-modifier: NEW  
                 | PUBLIC  
                 | PROTECTED  
                 | INTERNAL  
                 | PRIVATE  
                 | VIRTUAL  
                 | SEALED  
                 | OVERRIDE  
                 | ABSTRACT  
                 | EXTERN  
indexer-declarator: type  THIS  L_BRACKET  formal-parameter-list  R_BRACKET  
                   | type  interface-type  PERIOD  THIS  L_BRACKET  formal-parameter-list  R_BRACKET  
operator-declaration: attributes-opt  operator-modifiers  operator-declarator  operator-body  
operator-modifiers: operator-modifier  
                   | operator-modifiers  operator-modifier  
operator-modifier: PUBLIC  
                  | STATIC  
                  | EXTERN  
operator-declarator: unary-operator-declarator  
                    | binary-operator-declarator  
                    | conversion-operator-declarator  
unary-operator-declarator: type  OPERATOR  overloadable-unary-operator  L_PAREN  type  identifier  R_PAREN  
                          | overloadable-unary-operator:  one  of  
                          | PLUS  MINUS  L_NOT  NOT  PLUS_PLUS  MINUS_MINUS  TRUE  FALSE  
binary-operator-declarator: type  OPERATOR  overloadable-binary-operator  L_PAREN  type  identifier  COMMA  type  identifier  R_PAREN  
                           | overloadable-binary-operator:  one  of  
                           | PLUS  MINUS  TIMES  DIVIDE  MOD  AND  OR  XOR  L_SHIFT  R_SHIFT  EQ  NE  GT  LT  GE  LE  
conversion-operator-declarator: IMPLICIT  OPERATOR  type  L_PAREN  type  identifier  R_PAREN  
                               | EXPLICIT  OPERATOR  type  L_PAREN  type  identifier  R_PAREN  
operator-body: block  
              | SEMI  
constructor-declaration: attributes-opt  constructor-modifiers-opt  constructor-declarator  constructor-body  
constructor-modifiers: constructor-modifier  
                      | constructor-modifiers  constructor-modifier  
constructor-modifier: PUBLIC  
                     | PROTECTED  
                     | INTERNAL  
                     | PRIVATE  
                     | EXTERN  
constructor-declarator: identifier  L_PAREN  formal-parameter-list-opt  R_PAREN  constructor-initializer-opt  
constructor-initializer: COLON  BASE  L_PAREN  argument-list-opt  R_PAREN  
                        | COLON  THIS  L_PAREN  argument-list-opt  R_PAREN  
constructor-body: block  
                 | SEMI  
static-constructor-declaration: attributes-opt  static-constructor-modifiers  identifier  L_PAREN  R_PAREN  static-constructor-body  
                               | static-constructor-modifiers  
                               | extern-opt  STATIC  
                               | STATIC  extern-opt  
static-constructor-body: block  
                        | SEMI  
destructor-declaration: attributes-opt  extern-opt  NOT  identifier  L_PAREN  R_PAREN  destructor-body  
destructor-body: block  
                | SEMI  

##################################################
# C.2.8 Structs

struct-declaration: attributes-opt  struct-modifiers-opt  STRUCT  identifier  struct-interfaces-opt  struct-body  ;opt  
struct-modifiers: struct-modifier  
                 | struct-modifiers  struct-modifier  
struct-modifier: NEW  
                | PUBLIC  
                | PROTECTED  
                | INTERNAL  
                | PRIVATE  
struct-interfaces: COLON  interface-type-list  
struct-body: L_BRACE  struct-member-declarations-opt  R_BRACE  
struct-member-declarations: struct-member-declaration  
                           | struct-member-declarations  struct-member-declaration  
struct-member-declaration: constant-declaration  
                          | field-declaration  
                          | method-declaration  
                          | property-declaration  
                          | event-declaration  
                          | indexer-declaration  
                          | operator-declaration  
                          | constructor-declaration  
                          | static-constructor-declaration  
                          | type-declaration  

##################################################
# C.2.9 Arrays

array-type: non-array-type  rank-specifiers  
non-array-type: type  
rank-specifiers: rank-specifier  
                | rank-specifiers  rank-specifier  
rank-specifier: L_BRACKET  dim-separators-opt  R_BRACKET  
dim-separators: COMMA  
               | dim-separators  COMMA  
array-initializer: L_BRACE  variable-initializer-list-opt  R_BRACE  
                  | L_BRACE  variable-initializer-list  COMMA  R_BRACE  
variable-initializer-list: variable-initializer  
                          | variable-initializer-list  COMMA  variable-initializer  
variable-initializer: expression  
                     | array-initializer  

##################################################
# C.2.10 Interfaces

interface-declaration: attributes-opt  interface-modifiers-opt  INTERFACE  identifier  interface-base-opt  interface-body  ;opt  
interface-modifiers: interface-modifier  
                    | interface-modifiers  interface-modifier  
interface-modifier: NEW  
                   | PUBLIC  
                   | PROTECTED  
                   | INTERNAL  
                   | PRIVATE  
interface-base: COLON  interface-type-list  
interface-body: L_BRACE  interface-member-declarations-opt  R_BRACE  
interface-member-declarations: interface-member-declaration  
                              | interface-member-declarations  interface-member-declaration  
interface-member-declaration: interface-method-declaration  
                             | interface-property-declaration  
                             | interface-event-declaration  
                             | interface-indexer-declaration  
interface-method-declaration: attributes-opt  new-opt  return-type  identifier  L_PAREN  formal-parameter-list-opt  R_PAREN  SEMI  
interface-property-declaration: attributes-opt  new-opt  type  identifier  L_BRACE  interface-accessors  R_BRACE  
interface-accessors: attributes-opt  get  SEMI  
                    | attributes-opt  set  SEMI  
                    | attributes-opt  get  SEMI  attributes-opt  set  SEMI  
                    | attributes-opt  set  SEMI  attributes-opt  get  SEMI  
interface-event-declaration: attributes-opt  new-opt  EVENT  type  identifier  SEMI  
interface-indexer-declaration: attributes-opt  new-opt  type  THIS  L_BRACKET  formal-parameter-list  R_BRACKET  L_BRACE  interface-accessors  R_BRACE  

##################################################
# C.2.11 Enums

enum-declaration: attributes-opt  enum-modifiers-opt  ENUM  identifier  enum-base-opt  enum-body  ;opt  
enum-base: COLON  integral-type  
enum-body: L_BRACE  enum-member-declarations-opt  R_BRACE  
          | L_BRACE  enum-member-declarations  COMMA  R_BRACE  
enum-modifiers: enum-modifier  
               | enum-modifiers  enum-modifier  
enum-modifier: NEW  
              | PUBLIC  
              | PROTECTED  
              | INTERNAL  
              | PRIVATE  
enum-member-declarations: enum-member-declaration  
                         | enum-member-declarations  COMMA  enum-member-declaration  
enum-member-declaration: attributes-opt  identifier  
                        | attributes-opt  identifier  EQUALS  constant-expression  

##################################################
# C.2.12 Delegates

delegate-declaration: attributes-opt  delegate-modifiers-opt  DELEGATE  return-type  identifier  L_PAREN  formal-parameter-list-opt  R_PAREN  SEMI  
delegate-modifiers: delegate-modifier  
                   | delegate-modifiers  delegate-modifier  
delegate-modifier: NEW  
                  | PUBLIC  
                  | PROTECTED  
                  | INTERNAL  
                  | PRIVATE  

##################################################
# C.2.13 Attributes

global-attributes: global-attribute-sections  
global-attribute-sections: global-attribute-section  
                          | global-attribute-sections  global-attribute-section  
global-attribute-section: L_BRACKET  global-attribute-target-specifier  attribute-list  R_BRACKET  
                         | L_BRACKET  global-attribute-target-specifier  attribute-list  ,]  
global-attribute-target-specifier: global-attribute-target  COLON  
global-attribute-target: assembly  
                        | module  
attributes: attribute-sections  
attribute-sections: attribute-section  
                   | attribute-sections  attribute-section  
attribute-section: L_BRACKET  attribute-target-specifier-opt  attribute-list  R_BRACKET  
                  | L_BRACKET  attribute-target-specifier-opt  attribute-list  COMMA  R_BRACKET  
attribute-target-specifier: attribute-target  COLON  
attribute-target: field  
                 | EVENT  
                 | method  
                 | param  
                 | property  
                 | RETURN  
                 | type  
attribute-list: attribute  
               | attribute-list  COMMA  attribute  
attribute: attribute-name  attribute-arguments-opt  
attribute-name: type-name  
attribute-arguments: L_PAREN  positional-argument-list-opt  R_PAREN  
                    | L_PAREN  positional-argument-list  COMMA  named-argument-list  R_PAREN  
                    | L_PAREN  named-argument-list  R_PAREN  
positional-argument-list: positional-argument  
                         | positional-argument-list  COMMA  positional-argument  
positional-argument: attribute-argument-expression  
named-argument-list: named-argument  
                    | named-argument-list  COMMA  named-argument  
named-argument: identifier  EQUALS  attribute-argument-expression  
attribute-argument-expression: expression  

##################################################
# C.2.31 Opt

dim-separators-opt: dim-separators  
                   | empty  
argument-list-opt: argument-list  
                  | empty  
argument-list-opt: argument-list  
                  | empty  
rank-specifiers-opt: rank-specifiers  
                    | empty  
array-initializer-opt: array-initializer  
                      | empty  
statement-list-opt: statement-list  
                   | empty  
switch-sections-opt: switch-sections  
                    | empty  
for-initializer-opt: for-initializer  
                    | empty  
for-condition-opt: for-condition  
                  | empty  
for-iterator-opt: for-iterator  
                 | empty  
expression-opt: expression  
               | empty  
expression-opt: expression  
               | empty  
general-catch-clause-opt: general-catch-clause  
                         | empty  
specific-catch-clauses-opt: specific-catch-clauses  
                           | empty  
identifier-opt: identifier  
               | empty  
using-directives-opt: using-directives  
                     | empty  
global-attributes-opt: global-attributes  
                      | empty  
namespace-member-declarations-opt: namespace-member-declarations  
                                  | empty  
using-directives-opt: using-directives  
                     | empty  
namespace-member-declarations-opt: namespace-member-declarations  
                                  | empty  
attributes-opt: attributes  
               | empty  
class-modifiers-opt: class-modifiers  
                    | empty  
class-base-opt: class-base  
               | empty  
class-member-declarations-opt: class-member-declarations  
                              | empty  
attributes-opt: attributes  
               | empty  
constant-modifiers-opt: constant-modifiers  
                       | empty  
attributes-opt: attributes  
               | empty  
field-modifiers-opt: field-modifiers  
                    | empty  
attributes-opt: attributes  
               | empty  
method-modifiers-opt: method-modifiers  
                     | empty  
formal-parameter-list-opt: formal-parameter-list  
                          | empty  
attributes-opt: attributes  
               | empty  
parameter-modifier-opt: parameter-modifier  
                       | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
property-modifiers-opt: property-modifiers  
                       | empty  
set-accessor-declaration-opt: set-accessor-declaration  
                             | empty  
get-accessor-declaration-opt: get-accessor-declaration  
                             | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
event-modifiers-opt: event-modifiers  
                    | empty  
attributes-opt: attributes  
               | empty  
event-modifiers-opt: event-modifiers  
                    | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
indexer-modifiers-opt: indexer-modifiers  
                      | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
constructor-modifiers-opt: constructor-modifiers  
                          | empty  
formal-parameter-list-opt: formal-parameter-list  
                          | empty  
constructor-initializer-opt: constructor-initializer  
                            | empty  
argument-list-opt: argument-list  
                  | empty  
argument-list-opt: argument-list  
                  | empty  
attributes-opt: attributes  
               | empty  
extern-opt: EXTERN  
           | empty  
extern-opt: EXTERN  
           | empty  
attributes-opt: attributes  
               | empty  
extern-opt: EXTERN  
           | empty  
attributes-opt: attributes  
               | empty  
struct-modifiers-opt: struct-modifiers  
                     | empty  
struct-interfaces-opt: struct-interfaces  
                      | empty  
struct-member-declarations-opt: struct-member-declarations  
                               | empty  
dim-separators-opt: dim-separators  
                   | empty  
variable-initializer-list-opt: variable-initializer-list  
                              | empty  
attributes-opt: attributes  
               | empty  
interface-modifiers-opt: interface-modifiers  
                        | empty  
interface-base-opt: interface-base  
                   | empty  
interface-member-declarations-opt: interface-member-declarations  
                                  | empty  
attributes-opt: attributes  
               | empty  
new-opt: NEW  
        | empty  
formal-parameter-list-opt: formal-parameter-list  
                          | empty  
attributes-opt: attributes  
               | empty  
new-opt: NEW  
        | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
new-opt: NEW  
        | empty  
attributes-opt: attributes  
               | empty  
new-opt: NEW  
        | empty  
attributes-opt: attributes  
               | empty  
enum-modifiers-opt: enum-modifiers  
                   | empty  
enum-base-opt: enum-base  
              | empty  
enum-member-declarations-opt: enum-member-declarations  
                             | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
attributes-opt: attributes  
               | empty  
delegate-modifiers-opt: delegate-modifiers  
                       | empty  
formal-parameter-list-opt: formal-parameter-list  
                          | empty  
attribute-target-specifier-opt: attribute-target-specifier  
                               | empty  
attribute-target-specifier-opt: attribute-target-specifier  
                               | empty  
attribute-arguments-opt: attribute-arguments  
                        | empty  
positional-argument-list-opt: positional-argument-list  
                             | empty  
                             | 
                             | 

