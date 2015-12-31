"""Computes the product of two integers in string format.

"""


def int_mult(x, y):
    """Multiplies x and y, and returns their product.

    The int_mult function is intended to be
    called recursively in a divide-and-conquer
    approach of integer multiplication.

    x: string (decimal integer)
    y: string (decimal integer)

    Returns: string (decimal integer)
    """

    x_len = len(x)
    y_len = len(y)
    n = max(x_len, y_len)  # Maximum number of digits

    if x_len < 2 or y_len < 2:
        return str(int(x) * int(y))

    m = min(n // 2, x_len - 1, y_len - 1)
    x_left = x[:x_len - m]
    x_right = x[x_len - m:]
    y_left = y[:y_len - m]
    yRight = y[y_len - m:]

    p1 = int_mult(x_left, y_left)
    p2 = int_mult(x_right, yRight)
    p3 = int_mult(str_sum(x_left, x_right), str_sum(y_left, yRight))
    p = str_sum(
        p1 + '0'*2*m,
        str_sum(str_sum(str_sum(p3, '-' + p1), '-' + p2) + '0'*m, p2)
    )
    return p


def str_sum(a_str, b_str):
    """Returns sum of integer values of string arguments.

    a_str: string (decimal integer)
    b_str: string (decimal integer)

    Returns: string (decimal integer)
    """

    a = int(a_str)
    b = int(b_str)
    s_str = str(a + b)

    return s_str
