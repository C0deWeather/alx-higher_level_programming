#!/usr/bin/node

const { argv } = require('node:process');

let count = 0;
for (const arg of argv) {
  count++;
  if (count === 3) {
    console.log(arg);
  }
}
if (count <= 2) {
  console.log('No argument');
}
