#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const dict = {};
    for (const i in data) {
      const job = data[i];
      if (job.completed === true) {
        if (dict[job.userId] === undefined) {
          dict[job.userId] = 1;
        } else {
          dict[job.userId]++;
        }
      }
    }
    console.log(dict);
  }
});
