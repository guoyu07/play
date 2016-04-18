var bin = new Buffer([0x68, 0x65]);

console.log(bin[0]);

var str = bin.toString('utf-8');
console.log(str);

var bin = new Buffer('hello', 'utf-8');

console.log(bin.slice(2).toString('utf-8'));

console.log(bin.length);
