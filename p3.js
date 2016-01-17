const fs = require('fs');
const dict = {
    PLUS: '+',
    MINUS: '-',
    TIMES: '*',
    DIVIDE: '/',
    MOD: '%',
    OR: '|',
    AND: '&',
    NOT: '~',
    XOR: '^',
    L_SHIFT: '<<',
    R_SHIFT: '>>',
    L_OR: '||',
    L_AND: '&&',
    L_NOT: '!',
    LT: '<',
    GT: '>',
    LE: '<=',
    GE: '>=',
    EQ: '==',
    NE: '!=',


    EQUALS: '=',
    TIMES_EQUAL: '*=',
    DIV_EQUAL: '/=',
    MOD_EQUAL: '%=',
    PLUS_EQUAL: '+=',
    MINUS_EQUAL: '-=',
    L_SHIFT_EQUAL: '<<=',
    R_SHIFT_EQUAL: '>>=',
    AND_EQUAL: '&=',
    OR_EQUAL: '|=',
    XOR_EQUAL: '^=',
    PLUS_PLUS: '++',
    MINUS_MINUS: '--',
    CONDOP: '?',
    L_PAREN: '(',
    R_PAREN: ')',
    L_BRACKET: '[',
    R_BRACKET: ']',
    L_BRACE: '{',
    R_BRACE: '}',
    COMMA: ',',
    PERIOD: '.',
    SEMI: ';',
    COLON: ':',

    ABSTRACT: 'abstract',
    AS: 'as',
    BASE: 'base',
    BOOL: 'bool',
    BREAK: 'break',
    BYTE: 'byte',
    CASE: 'case',
    CATCH: 'catch',
    CHAR: 'char',
    CHECKED: 'checked',
    CLASS: 'class',
    CONST: 'const',
    CONTINUE: 'continue',
    DECIMAL: 'decimal',
    DEFAULT: 'default',
    DELEGATE: 'delegate',
    DO: 'do',
    DOUBLE: 'double',
    ELSE: 'else',
    ENUM: 'enum',
    EVENT: 'event',
    EXPLICIT: 'explicit',
    EXTERN: 'extern',
    FALSE: 'false',
    FINALLY: 'finally',
    FIXED: 'fixed',
    FLOAT: 'float',
    FOR: 'for',
    FOREACH: 'foreach',
    GOTO: 'goto',
    IF: 'if',
    IMPLICIT: 'implicit',
    IN: 'in',
    INT: 'int',
    INTERFACE: 'interface',
    INTERNAL: 'internal',
    IS: 'is',
    LOCK: 'lock',
    LONG: 'long',
    NAMESPACE: 'namespace',
    NEW: 'new',
    NULL: 'null',
    OBJECT: 'object',
    OPERATOR: 'operator',
    OUT: 'out',
    OVERRIDE: 'override',
    PARAMS: 'params',
    PRIVATE: 'private',
    PROTECTED: 'protected',
    PUBLIC: 'public',
    READONLY: 'readonly',
    REF: 'ref',
    RETURN: 'return',
    SBYTE: 'sbyte',
    SEALED: 'sealed',
    SHORT: 'short',
    SIZEOF: 'sizeof',
    STACKALLOC: 'stackalloc',
    STATIC: 'static',
    STRING: 'string',
    STRUCT: 'struct',
    SWITCH: 'switch',
    THIS: 'this',
    THROW: 'throw',
    TRUE: 'true',
    TRY: 'try',
    TYPEOF: 'typeof',
    UINT: 'uint',
    ULONG: 'ulong',
    UNCHECKED: 'unchecked',
    UNSAFE: 'unsafe',
    USHORT: 'ushort',
    USING: 'using',
    VIRTUAL: 'virtual',
    VOID: 'void',
    VOLATILE: 'volatile',
    WHILE: 'while'

};

var rulesAddition = '';

var fileName = process.argv[2];

var lines = fs.readFileSync(fileName).toString().split('\n');
var out = '';
var len = 0, isDef = false;
for (var line of lines) {
    line = line.trim();

    if (/^C\.2\.\d\d?/.test(line)) {
        out += '\n'+'#'.repeat(50)+'\n# '+line + '\n\n';
    } else {
        if (/^\w+(-\w+)*:$/.test(line)) {
            len = line.length;
            isDef = true;
            var def  = line.substr(0, len - 1); 
            out += '    """\n    pass\ndef p_' + def + '(p):\n    """\n';
            out += '    ' + def + ' :';
        } else {
            if (isDef) {
                out += " " + Stm(line) + '\n';
                isDef = false;
            } else {
                
                out += '    '+' '.repeat(len) + "| "+  Stm(line) + '\n';
            }
        }
    }

    //line = line.replace(/opt/g, '_');
}
// out += out.replace(/-/g, '_');
console.log(out);


function Stm(st) {
    var a = st.split(' ');
    var o = '';
    for (var e in a) {
        var s = a[e].trim();
        if (!s) {
            continue;
        }


        if (/\w+opt$/.test(s)) {
            // console.log(s);
            var s1 = s.substr(0, s.length - 3);
            s = s1 + '-opt';
            rulesAddition += s + ':\n' + s1 + '\nempty\n'
        } else {
            for (var key in dict) {
                if (dict[key] == s) {
                    s = key;
                    break;
                }
            }
        }

        o += s + '  ';
    }

    return o;
}

// console.log('C.2.31 Opt\n'+rulesAddition);
// var str = '[ \'  attribute-target-specifieropt  , ; " attribute-list   ]';

// console.log(Stm(str));