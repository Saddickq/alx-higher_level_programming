#!/usr/bin/node
const myArr = require('./100-data').list;

const newArr = myArr.map((num, index) => num * index);
console.log(myArr);
console.log(newArr);