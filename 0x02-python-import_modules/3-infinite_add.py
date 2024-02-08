#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    total = 0

    for arg in args:
        total += int(arg)

    print(total)

'''
 sum = 0
    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
'''