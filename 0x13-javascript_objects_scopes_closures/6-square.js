#!/usr/bin/node
const S = require('./5-square');

class Square extends S {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i = i + 1) {
      for (let j = 0; j < this.width; j = j + 1) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
}
module.exports = Square;
