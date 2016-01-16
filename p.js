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
    COMMA: ',',
    PERIOD: '.',
    SEMI: ';',
    COLON: ':'

};


var fileName = process.argv[2];

var lines = fs.readFileSync(fileName).toString().split('\n');
var out = '';
for (var line of lines) {
    line = line.trim();

    if (/^C\.2\.\d\d?/.test(line)) {
        out += line + '\n';
    } else {
        if (/^\w+(-\w+)*:$/.test(line)) {
            out += "\t" + line + '\n';
        } else {
            out += "\t\t" + Stm(line) + '\n';
        }
    }

    //line = line.replace(/opt/g, '_');
}
out += out.replace(/-/g, '_');
console.log(out);

function Stm(st) {
    var a = st.split(' ');
    var o = '';
    for (var e in a) {
        var s = a[e].trim();
        if (!s) {
            continue;
        }

        for (var key in dict) {
            if (dict[key] == s) {
                s = key;
                break;
            }
        }

        o += s + '  ';
    }

    return o;
}


// var str = '[ \'  attribute-target-specifieropt  , ; " attribute-list   ]';

// console.log(Stm(str));