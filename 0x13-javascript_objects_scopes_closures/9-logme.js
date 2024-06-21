#!/usr/bin/node
class cls {
  static count = 0;

  static logme (item) {
    console.log(`${cls.count}: ${item}`);
    cls.count++;
  }
}
exports.logMe = cls.logme;
