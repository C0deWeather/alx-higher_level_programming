#!/usr/bin/node

const { argv } = require('node:process');

const n = Number(argv[2]);
if (isNaN(n)) {
  console.log('Not a number');
} else {
  console.log(n);
}
