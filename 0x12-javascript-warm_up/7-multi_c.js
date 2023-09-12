#!/usr/bin/node
let arg = parseInt(process.argv[2], 10);

if (isNaN(arg) === false) {
    while (arg > 0) {
        console.log("C is fun");
        arg--;
    }
} else {
    console.log("Missing number of occurrences");
}