# ----------------------------------------------------------------------
# clex.py
#
# A lexer for ANSI C.
# ----------------------------------------------------------------------



import ply.lex as lex

# Reserved words
reserved = (
    'USING','NAMESPACE', 'PUBLIC', 'PRIVATE', 'INT', 'DOUBLE', 'BOOL', 'VOID',
    )

tokens = reserved + (
    'ID',
    )
literals = ['+', '-', '*', '/', '(', ')', '.', ';', '{', '}']
# Completely ignored characters
t_ignore           = ' \t\x0c'

# Newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    


reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"ID")
    return t

def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)
    
lexer = lex.lex()
if __name__ == "__main__":
    lex.runmain(lexer)

    



