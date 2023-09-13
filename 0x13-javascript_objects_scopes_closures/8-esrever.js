#!/usr/bin/node
exports.esrever = function (list) {
    let lastIndex = list.length - 1;
    let reversedList = [];
    let j = 0;
    for (let i = lastIndex; i >= 0; i--) {
        reversedList[j] = list[i];
        j++;
    }
    return reversedList;
}