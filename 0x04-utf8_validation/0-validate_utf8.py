#!/usr/bin/python3

""" method that determines if a given data
set represents a valid UTF-8 encoding
"""


def validUTF8(data):

    num_byte = 0

    sig_1 = 1 << 7
    sig_2 = 1 << 6

    for i in data:

        sig_int = 1 << 7

        if num_byte == 0:

            while sig_int & i:
                num_byte += 1
                sig_int = sig_int >> 1

            if num_byte == 0:
                continue

            if num_byte == 1 or num_byte > 4:

                return False
        else:

            if not (i & sig_1 and not (i & sig_2)):
                return False
        num_byte -= 1
    if num_byte == 0:
        return True

    return False
