#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const castmembers = JSON.parse(body).characters;
    printCharacters(castmembers, 0);
  }
});

function printCharacters (castmembers, index) {
  request(castmembers[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < castmembers.length) {
        printCharacters(castmembers, index + 1);
      }
    }
  });
}
