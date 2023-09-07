#!/usr/bin/python3
for x in reversed(range(97, 123)):
    print("{:c}".format(x if (x % 2 == 0) else (x - 32)), end='')
