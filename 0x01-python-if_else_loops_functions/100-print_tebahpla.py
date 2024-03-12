#!/usr/bin/python3
i = 1
offset = ord('a') - ord('A')
for char in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        char -= offset
    print("{}".format(chr(char)), end="")
    i += 1
