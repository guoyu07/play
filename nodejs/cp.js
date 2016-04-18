var fs = require('fs');

var copy = function (src, dst) {
    fs.writeFileSync(dst, fs.readFileSync(src));
}

var main = function (argv) {
    copy(argv[0], argv[1]);
}

main(process.argv.slice(2));
