#!/usr/bin/python3
"""validates a UTF-8"""


def validUTF8(data):
    """determines if a given data set
    represents a valid UTF-8 encoding.

    Args:
        data (int): the integers to be validated
    """
    num_bytes = 0

    for byte in data:
        # Check if the byte is a continuation byte
        if num_bytes == 0:
            if (byte & 128) == 0:
                num_bytes = 0
            elif (byte & 224) == 192:
                num_bytes = 1
            elif (byte & 240) == 224:
                num_bytes = 2
            elif (byte & 248) == 240:
                num_bytes = 3
            else:
                return False
        else:
            # Check if the byte is a continuation byte
            if (byte & 193) != 128:
                return False
            num_bytes -= 1
    # If there are still bytes to read, the encoding is invalid
    if num_bytes == 0:
        return True

    return False
