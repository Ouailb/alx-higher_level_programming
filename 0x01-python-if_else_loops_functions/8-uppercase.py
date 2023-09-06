#!/usr/bin/python3
def uppercase(s):
    num = ord('a') - ord('A')
    for char in s:
        if 'a' <= char <= 'z':
            print("{:c}".format(ord(char) - num), end='')
        else:
            print(char, end='')

