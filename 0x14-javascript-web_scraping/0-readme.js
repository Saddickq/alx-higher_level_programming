#!/usr/bin/node

const fileName = process.argv[2];

const fs = require('fs');

fs.readFile(fileName, 'utf-8', (error, data) => {
  if (error) console.log(error);
  console.log(data);
});
