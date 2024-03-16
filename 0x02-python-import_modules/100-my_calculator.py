#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) - 1 != 3:
        print(f"Usage: ./100-calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {'+': add, '-': sub, '*': mul, '/': div}
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    for op in ops:
        if sys.argv[2] == op:
            print(f"{a} {op} {b} = {ops[op](a, b)}")
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
