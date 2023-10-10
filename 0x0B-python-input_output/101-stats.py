#!/usr/bin/python3

""" Reads from standard input and computes metrics """


import signal
import sys


def print_stats(signum, frame):
    """Print accumulated metrics."""
    total_size = sum(file_sizes)
    print("File size: {}".format(total_size))

    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


signal.signal(signal.SIGINT, print_stats)

status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

file_sizes = []

line_count = 0

for line in sys.stdin:
    parts = line.split()
    if len(parts) > 2:
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        if status_code in status_codes:
            status_codes[status_code] += 1

        file_sizes.append(file_size)
        line_count += 1

        if line_count == 10:
            print_stats(0, 0)
            line_count = 0

print_stats(0, 0)
