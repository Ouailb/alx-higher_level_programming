#!/usr/bin/python3
def uppercase(s):
    num = ord('a') - ord('A')  # Calculate the difference between lowercase and uppercase ASCII values
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += "{:c}".format(ord(char) - num)
        else:
            result += char
    print(result)
    print()

