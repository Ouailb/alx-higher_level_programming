#!/usr/bin/python3
def uppercase(x):
    for i in range(len(x)):
        if ord(x[i]) >= 97 and ord(x[i]) <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(x[i]) - num), end='')
    print()
