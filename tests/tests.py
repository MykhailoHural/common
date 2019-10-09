import unittest
import math
from homework import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_perimeter(self):
        self.rectangle = Rectangle(1, 4)
        self.assertEqual(self.rectangle, 10)
    

        


'''

    def test_get_rectangle_square(self):
        self.assertTrue(type(get_rectangle_square), int or float)

    def test_get_rectangle_diagonal(self):
        self.assertGreaterEqual(get_rectangle_diagonal, 0)
'''

if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
