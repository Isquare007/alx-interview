const fs = require('fs');

(async () => {
    const writeStream = fs.createWriteStream(out.csv);

    for (let i = 0; i<1e8; i++) {
        const overWatermark = writeStream.write(`${i}, 1\n`);

        if (!overWatermark) {
            await new Promise((resolve) => {
                writeStream.once('drain', resolve)
            })
        }
    }
})