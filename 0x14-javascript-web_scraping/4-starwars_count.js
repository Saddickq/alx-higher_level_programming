#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const charId = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const character = data.results.filter((movie) => movie.characters.includes(charId));
    console.log(character.length);
  }
});
