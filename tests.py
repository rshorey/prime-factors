import unittest
import prime_test as pt
import find_big_prime as fpb

class TestPrimeTest(unittest.TestCase):

    def test_prime_tester(self):
        self.assertFalse(pt.is_it_prime(-1))
        self.assertFalse(pt.is_it_prime(0))
        self.assertFalse(pt.is_it_prime(1))
        self.assertTrue(pt.is_it_prime(2))
        self.assertFalse(pt.is_it_prime(4))
        self.assertFalse(pt.is_it_prime(8))
        self.assertFalse(pt.is_it_prime(9))
        self.assertFalse(pt.is_it_prime(51))
        self.assertFalse(pt.is_it_prime(321))
        self.assertTrue(pt.is_it_prime(7))
        self.assertTrue(pt.is_it_prime(31))
        self.assertTrue(pt.is_it_prime(1999))
        self.assertTrue(pt.is_it_prime(8675309))


if __name__ == '__main__':
    unittest.main()