#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter ('a' to 'z')
        if 'a' <= char <= 'z':
            # Convert lowercase letter to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        print(uppercase_char, end='')
    print()
