#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${arg}`;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode, body);
    return;
  }
  const characterCount = 0;
  const charactersUrl = JSON.parse(body).characters;
  printName(charactersUrl, characterCount);
});
const printName = (url, count) => {
  request(url[count], (err, response, body) => {
    if (err) {
      console.log(err);
    }
    if (response.statusCode !== 200) {
      console.error('Error:', response.statusCode, body);
      return;
    }
    const characterName = JSON.parse(body).name;
    console.log(characterName);
    if (++count < url.length) {
      printName(url, count++);
    }
  });
};
