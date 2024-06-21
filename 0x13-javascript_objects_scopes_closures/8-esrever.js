#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  for (const e of list) {
    newList.unshift(e);
  }
  return newList;
};
