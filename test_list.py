import unittest
from lists import lists

class MyTestCase(unittest.TestCase):
    test = lists([1,2,3,4,5,6,7,-2,-67])
    def test_something(self):
        self.assertEqual(self.test, -67)
        self.assertTrue(self.test, int)


if __name__ == '__main__':
    unittest.main()
