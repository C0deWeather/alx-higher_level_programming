#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    r_sum = 0
    i = 0
    for argument in argv:
        if i == 0:
            i += 1
            continue
        r_sum += int(argument)
    print(r_sum)
