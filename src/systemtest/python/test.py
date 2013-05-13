import unittest

class Test(unittest.TestCase):

    def test_fails(self):
        self.assertEqual(0, 1)


if __name__ == '__main__':
    unittest.main()
