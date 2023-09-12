#!/usr/bin/node
const arg = parseInt(process.argv[2], 10);

if (isNaN(arg) === false) {
  for (let i = 0; i < arg; i++) {
    let line = '';
    for (let j = 0; j < arg; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
