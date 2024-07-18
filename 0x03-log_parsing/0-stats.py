#!/usr/bin/python3

import sys
import signal

# Initialize metrics
total_file_size = 0
counter = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

def print_msg(dict_sc, total_file_size):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C) and print metrics."""
    print_msg(dict_sc, total_file_size)
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parsed_line = line.split()
        if len(parsed_line) < 7:
            continue

        counter += 1

        try:
            total_file_size += int(parsed_line[-1])  # file size
            code = parsed_line[-2]  # status code

            if code in dict_sc:
                dict_sc[code] += 1
        except ValueError:
            continue

        if counter == 10:
            print_msg(dict_sc, total_file_size)
            counter = 0

finally:
    print_msg(dict_sc, total_file_size)
