#!/usr/bin/node
function secondLargestNumber (array) {
  const length = array.length;

  let largest = array[0];
  let secondLargest = 0;

  if (length < 2) {
    return (secondLargest);
  }
  for (let i = 1; i < length; i++) {
    if (array[i] > largest) {
      secondLargest = largest;
      largest = array[i];
    } else if (array[i] > secondLargest && array[i] !== largest) {
      secondLargest = array[i];
    }
  }
  return (secondLargest);
}

const myArray = process.argv.slice(2).map(Number);
// console.log(myArray);
const secondLargest = secondLargestNumber(myArray);
console.log(secondLargest);
