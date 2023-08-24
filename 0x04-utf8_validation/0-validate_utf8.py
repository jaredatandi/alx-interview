#!/bin/usr/env python3

"""A module to check for a valide utf8
"""


def validUTF8(data):
    """Valide the utf 8

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Helper function to check if a byte is a valid UTF-8 continuation byte
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    index = 0
    while index < len(data):
        # Get the number of bytes for the current character
        num_bytes = 0
        mask = 0b10000000
        while data[index] & mask:
            num_bytes += 1
            mask >>= 1
        if num_bytes == 0:
            num_bytes = 1

        # Check if the number of bytes is valid
        if num_bytes > 4 or num_bytes == 1:
            return False

        # Check if there are enough bytes left in the data
        if index + num_bytes > len(data):
            return False

        # Check if the following bytes are valid continuation bytes
        for i in range(1, num_bytes):
            if not is_continuation(data[index + i]):
                return False

        index += num_bytes

    return True
