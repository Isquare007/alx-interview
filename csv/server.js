const express = require("express");
const { parse } = require("csv");
const fs = require("fs");

const app = express();
app.use(express.json);
function createparser(name) {
  return parse({ columns: true }, function (err, records) {
    if (err) {
      console.error(err);
      return;
    }

    for (const record of records) {
      if (record["Name"] === name) {
        return record;
      }
    }
  });
}

app.get("/parse/:name", (req, res) => {
  const { name } = req.params;

  const parser = createparser(name);
  res.json(fs.createReadStream("sample-data.csv").pipe(parser));
});



app.listen(4000, () => {
  console.log("server running on port 4000");
});
