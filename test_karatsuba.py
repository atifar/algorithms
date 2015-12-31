from karatsuba import int_mult


def test_multiply_odd_by_1_length():
    a, b = 54320, 9
    assert int_mult(str(a), str(b)) == str(a * b)


def test_multiply_even_by_1_length():
    a, b = 543210, 5
    assert int_mult(str(a), str(b)) == str(a * b)


def test_multiply_odd_by_odd_length():
    a, b = 54320, 529
    assert int_mult(str(a), str(b)) == str(a * b)


def test_multiply_even_by_odd_length():
    a, b = 543210, 529
    assert int_mult(str(a), str(b)) == str(a * b)


def test_multiply_even_by_even_length():
    a, b = 543210, 5293
    assert int_mult(str(a), str(b)) == str(a * b)
