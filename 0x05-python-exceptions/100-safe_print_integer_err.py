#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        # Try to print the integer value
        print("{:d}".format(value))
        return True
    except Exception as e:
        # Print the exception message to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        return False
