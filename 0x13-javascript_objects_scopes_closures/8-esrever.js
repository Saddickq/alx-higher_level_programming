#!/usr/bin/node
exports.esrever = function (list) {
  const lastIndex = list.length - 1;
  const reversedList = [];
  let j = 0;
  for (let i = lastIndex; i >= 0; i--) {
    reversedList[j] = list[i];
    j++;
  }
  return reversedList;
};
