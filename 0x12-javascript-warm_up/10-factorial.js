#!/usr/bin/node
const num = parseInt(process.argv[2], 10);

function factorial (number) {
  if (isNaN(number) === true) {
    return 1;
  }
  if (number <= 1) {
    return 1;
  }
  return (number * factorial(number - 1));
}

console.log(factorial(num));
