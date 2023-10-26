#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const charId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const data = JSON.parse(body);
    data.results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes(charId)) count++;
      });
    });
    console.log(count);
  }
});
