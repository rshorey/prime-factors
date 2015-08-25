import unittest
import prime_test as pt
import find_big_prime as fbp

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

    def test_find_big_prime(self):
        #several times because it's random
        self.assertIn(fbp.find_big_prime(1), [2,3,5,7])
        self.assertIn(fbp.find_big_prime(1), [2,3,5,7])
        self.assertIn(fbp.find_big_prime(1), [2,3,5,7])
        self.assertIn(fbp.find_big_prime(1), [2,3,5,7])
        self.assertIn(fbp.find_big_prime(1), [2,3,5,7])

        two_digit_list = [11,13,17,19,23,29,31,
                          37,41,43,47,53,59,61,67,
                          71,73,79,83,89,97]

        self.assertIn(fbp.find_big_prime(2), two_digit_list)
        self.assertIn(fbp.find_big_prime(2), two_digit_list)
        self.assertIn(fbp.find_big_prime(2), two_digit_list)
        self.assertIn(fbp.find_big_prime(2), two_digit_list)
        self.assertIn(fbp.find_big_prime(2), two_digit_list)

if __name__ == '__main__':
    unittest.main()