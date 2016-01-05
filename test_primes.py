from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from primes import primes_between

PRIMES_2_TO_200 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                   53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
                   113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
                   181, 191, 193, 197, 199]


class PrimeGeneratorTest(TestCase):

    @staticmethod
    def get_expected_string(low, high):
        """Return space separated string of primes from low to <high"""
        primes = [str(p) for p in PRIMES_2_TO_200 if low <= p < high]
        return " ".join(primes)

    def test_one_prime_equals_range_low(self):
        low, high = 3, 4
        expected_output = self.get_expected_string(low, high)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            primes_between(low, high)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_one_prime_greater_than_range_low(self):
        low, high = 24, 30
        expected_output = self.get_expected_string(low, high)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            primes_between(low, high)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_zero_prime_in_range_above_2(self):
        low, high = 24, 29
        expected_output = self.get_expected_string(low, high)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            primes_between(low, high)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_range_below_2(self):
        low, high = 1, 6
        expected_output = ''
        with patch('sys.stdout', new=StringIO()) as fake_out:
            primes_between(low, high)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_primes_in_2_to_200(self):
        low, high = 2, 200
        expected_output = self.get_expected_string(low, high)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            primes_between(low, high)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)
