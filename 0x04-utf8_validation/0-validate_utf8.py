#!/usr/bin/python3
"""UTF-8 Validation Module"""


def validUTF8(data):
    """
    function that determines if a given data
    set represents a valid UTF-8 encoding.
    """
    bytes_number = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for number in data:
        mask_n_byte = 1 << 7
        if bytes_number == 0:
            while mask_n_byte & number:
                bytes_number += 1
                mask_n_byte = mask_n_byte >> 1
            if bytes_number == 0:
                continue
            if bytes_number == 1 or bytes_number > 4:
                return False
        else:
            if not (number & mask1 and not (number & mask2)):
                return False
        bytes_number -= 1
    return bytes_number == 0
