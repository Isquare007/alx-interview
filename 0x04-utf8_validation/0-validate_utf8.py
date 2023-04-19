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
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # Check if the byte is a continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
    # If there are still bytes to read, the encoding is invalid
    if num_bytes != 0:
        return False

    return True


data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
