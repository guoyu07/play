var path = require('path');

console.log(path.normalize('.//'));

var str = path.join('foo/', '/bar', 'test');
console.log(str);

console.log(path.extname('./hello.js'));
