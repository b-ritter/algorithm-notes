import unittest

from fibonacci import fib_slow, fib_fast

class TestFib(unittest.TestCase):
    def test_fib_slow(self):
        self.assertEqual(fib_slow(3), 2)
        self.assertEqual(fib_slow(4), 3)
        self.assertEqual(fib_slow(5), 5)
        self.assertEqual(fib_slow(6), 8)
    
    def test_fib_fast(self):
        self.assertEqual(fib_fast(3), 2)
        self.assertEqual(fib_fast(4), 3)
        self.assertEqual(fib_fast(5), 5)
        self.assertEqual(fib_fast(6), 8)