import math


def _is_prime(num):
    for j in range(2, int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True


def primes_between(low, high):
    """Finds the sequence of primes between 'low', inclusive and 'high',
    exclusive, then prints them separated by a space on a single line.
    Range limits are integers, such that 2 <= 'low' < 'high'.
    """
    if low < 2:
        return

    if (low == 2):
        print(2, end=" "),

    if (low % 2 == 0):
        low += 1

    for i in range(low, high, 2):
        if _is_prime(i):
            print(i, end=" "),
