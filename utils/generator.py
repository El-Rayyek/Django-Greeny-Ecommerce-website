import random


def generator(length = 8):
    code = ''.join(random.choice('1234567890') for _ in range(length))
    return code