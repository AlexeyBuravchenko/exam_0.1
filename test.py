import unittest
from programm import Progression


class MyTestCase(unittest.TestCase):
    test1 = Progression(3)
    test2 = Progression(7)
    test3 = Progression(8)
    test4 = Progression(2)
    test_error = Progression('str')

    def test(self):
        self.assertEqual(self.test1.n_element(), 8)
        self.assertEqual(self.test2.n_element(), 20)
        self.assertEqual(self.test3.n_element(), 23)
        self.assertEqual(self.test4.n_element(), 5)
        self.assertTrue(self.test1.n_element, isinstance(self.test, int))
        self.assertRaises(TypeError,self.test_error.n_element)


if __name__ == '__main__':
    unittest.main()
