#!/usr/bin/python3#!/usr/bin/python3
"""UTF-8 validation module"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding."""
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            # Count the number of leading 1's
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte character
            if n_bytes == 0:
                continue

            # If the count is more than 4 or equal to 1, it's invalid
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if it is a valid 10xxxxxx sequence
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1

    # If n_bytes is not zero at the end,
    # it means we have an incomplete character
    return n_bytes == 0
