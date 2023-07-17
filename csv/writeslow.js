const fs = require('fs');
const path = require('path')

const data = ['name,cost'];
const filePath = path.join(__dirname, 'out-space.csv');

for (let i = 0; i < 10; i++) {
    data.push(`${i}, ${i+1}`);
}
fs.writeFileSync(filePath, data.join('\n'))