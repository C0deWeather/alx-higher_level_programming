#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')


def uppercase(str):
    offset = ord('a') - ord('A')
    for i in range(len(str)):
        if islower(str[i]):
            c = chr(ord(str[i]) - offset)
        else:
            c = str[i]
        print("{}".format(c), end="")
    print("\n", end="")
