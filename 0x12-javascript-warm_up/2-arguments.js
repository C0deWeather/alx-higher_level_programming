#!/usr/bin/node
const { argv } = require('node:process');
if (argv.slice(2).length > 1) {
  console.log('Arguments found');
} else if (argv.slice(2).length === 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
