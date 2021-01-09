import unittest


class MyTestCase(unittest.TestCase):
    def test_fibonacci(self):
        from common import fibonacci
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)


if __name__ == '__main__':
    unittest.main()
