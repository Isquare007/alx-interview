const fs = require('fs');

const file  = fs.readFileSync('out-space.csv', 'utf-8');

const lines = file.trim('\n').split('\n');

lines.shift()

const sum = lines.reduce((acc, line) => {
    console.log(parseFloat(line.split(','[1])))
    return acc + parseFloat(line.split(','[1]))
    
}, 0);

console.log('sum', sum)