#!/usr/bin/env python3

import random

def alphaencode(number, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """Converts an integer to a alpha string."""
    alpha = ''
    sign = ''

    if number < 0:
        sign = '-'
        number = -number

    if 0 <= number < len(alphabet):
        return sign + alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        alpha = alphabet[i] + alpha

    return sign + alpha

print(
    alphaencode(
        random.getrandbits(32)
    )
)
