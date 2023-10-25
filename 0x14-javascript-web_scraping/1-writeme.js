#!/usr/bin/node

const fileName = process.argv[2];

const content = process.argv[3];

const fs = require('fs');

fs.writeFile(fileName, content, 'utf-8', (error) => {
  if (error) console.log(error);
});
