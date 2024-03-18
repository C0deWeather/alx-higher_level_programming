#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            item = "Fizz"
        elif i % 5 == 0 and i % 3 != 0:
            item = "Buzz"
        elif i % 3 == 0 and i % 5 == 0:
            item = "FizzBuzz"
        else:
            item = i
        print(item, end=" ")
