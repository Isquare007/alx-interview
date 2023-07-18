const express = require('express');
const {parse} = require('csv');
const fs = require('fs');

const app = express();

const parser = parse({columns:true}, function(err, records) {
    if (err) {
        console.error(err);
        return;
    }
    
    for (const record of records) {
        if (record['Name'] === 'Watkins-Kaiser') {
            console.log(record)
        }
    }

    const write = fs.writeFileSync('write.csv')
    write.write(records)
    // console.log(records.shift());
})

fs.createReadStream('sample-data.csv').pipe(parser)




app.use(express.json);

app.listen(4000, () => {
    console.log('server running on port 4000');
})