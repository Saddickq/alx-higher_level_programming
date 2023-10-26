#!/usr/bin/node

const request = require('request');

const fs = require('fs');

const apiUrl = process.argv[2];

const fileName = process.argv[3];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileName, body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
