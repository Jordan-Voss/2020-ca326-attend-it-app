import unittest
from student import is_prime

class PrimesTestCase(unittest.TestCase):

    def test_5_prime(self):
        self.assertTrue(is_prime(5))


if __name__ == '__main__':
    unittest.main()
