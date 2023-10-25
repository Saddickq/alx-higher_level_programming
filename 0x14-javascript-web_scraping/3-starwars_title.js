#!/usr/bin/node

const request = require('request');

const movieId = parseInt(process.argv[2], 10);

const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    try {
      const data = JSON.parse(body);
      const resultsDict = data.results;
      for (const dictionary of resultsDict) {
        if (dictionary.episode_id === movieId) {
          console.log(dictionary.title);
        }
      }
    } catch (parseError) {
      console.log(parseError);
    }
  }
});
