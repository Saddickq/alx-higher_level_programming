#!/usr/bin/node
const dict = require('./101-data').dict;

newDict = {};
for (const key in dict) {
    const value = dict[key];
    if (newDict[value] === undefined) {
        newDict[value] = [];
        newDict[value].push(key);
    } else {
        newDict[value].push(key);
    }
}
console.log(newDict);
