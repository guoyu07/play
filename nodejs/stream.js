var fs = require('fs');
var rs = fs.createReadStream('./1');

rs.on('data', function (chunck) {
    console.log(chunck);
});

rs.on('end', function () {
    console.log('end');
});
