#!/usr/bin/python3

import sys

text = "and that piece of art is useful"
name = "Dora Korpar"
date = (2015, 10, 19)

sys.stderr.write(f"{text} - {name}, {date[0]}-{date[1]}-{date[2]}\n")

sys.exit(1)
