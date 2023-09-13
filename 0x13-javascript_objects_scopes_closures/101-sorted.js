#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
for (key in dict) {
  const value = key;
  if (!newDict[value]) {
    newDict[value] = [];
    newDict[value].push(key);
  } else {
    newDict[value].push(key);
  }
}
console.log(dict);
console.log(newDict);
