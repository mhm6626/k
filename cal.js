function C(y, m, d) {
    var dom = (new Date(y, m + 1, 1) - new Date(y, m, 1)) / 1000 / 3600 / 24;

    var f = new Date(y, m, 1);
    var x = f.getDay();
    var out = '';

    for (var i = 0; i < (x + dom); i++) {
        if (i % 7 == 0) {
            out += '\n';
        }
        if (i < x) {
            out += '\t|';
        } else {
            var day = (i - x + 1);
            if (day == d) {
                out += '*';
            }
            out += day + '\t|';
        }
    }

    console.log(out)
}

C(2016, 1, 5);