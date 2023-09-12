#!/usr/bin/node
const argument = parseInt(process.argv[2], 10)

if (isNaN(argument) === false) {
    console.log("My number: " + argument);
} else {
    console.log("Not a number");
}