#!/usr/bin/node

exports.converter = function (base) {
  return function h (n) {
    return n.toString(base);
  };
};
