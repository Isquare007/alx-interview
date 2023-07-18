const axios = require('axios');

axios.get('https://coderbyte.com/api/challenges/logs/user-info-csv').then(res => {
  const data = res.data;
  let json = [];

  const lines = data.trim().split('\n');
  const headers = lines.shift().split(',');
  
  for (let l = 0; l < lines.length; l++) {
    const rowData = lines[l].split(',');
    let obj = {}

    for (let r = 0; r < rowData.length; r++) {
      const key = headers[r].trim();
      const value = rowData[r].trim();
      obj[key] = value ;
      // if ((r + 1) === 3) {
      //   json.push(arrObj)
      //   arrObj = {}
      // }
    }
    json.push(obj);
  }
  json.sort((a, b) => {
    const aKeys = Object.keys(a);
    const bkeys = Object.keys(b);
    return a[aKeys[1]].localeCompare(b[bkeys[1]]);
  })
  console.log(JSON.stringify(json));
})