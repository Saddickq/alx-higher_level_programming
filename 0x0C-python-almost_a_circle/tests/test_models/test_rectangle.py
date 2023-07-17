#!/usr/bin/python3
"""
unittest module for the Rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test cases for Rectangle class """
    # test width_private
    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 0, 0, 1).__width)

    # normal test
    def test_width(self):
        w1 = Rectangle(1, 2)
        self.assertEqual(w1.width, 1)

    # test_width_getter
    def test_width_getter(self):
        w2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(w2.width, 1)

    # test_width_setter
    def test_width_setter(self):
        w3 = Rectangle(1, 2, 3, 4)
        w3.width = 5
        self.assertEqual(w3.width, 5)

    # test_width_None
    def test_width_None(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(None, 2)

    # test_width_zero
    def test_width_zero(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 2)

    # test_width_negative
    def test_width_negative(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-1, 2)

    # test_width_float
    def test_width_float(self):
        self.assertRaises(TypeError, lambda: Rectangle(1.5, 2))

    # test_height_private
    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 0, 0, 1).__height)

    # test_normal
    def test_height(self):
        h1 = Rectangle(1, 2)
        self.assertEqual(h1.height, 2)

    # test_height_getter
    def test_height_getter(self):
        h2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(h2.height, 2)

    # test_height_setter
    def test_height_setter(self):
        h3 = Rectangle(1, 2, 3, 4)
        h3.height = 10
        self.assertEqual(h3.height, 10)

    # test_height_None
    def test_height_None(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, None)

    # test_height_zero
    def test_height_zero(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, 0)

    # test_height_negative
    def test_height_negative(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, -2)

    # test_height_float
    def test_height_float(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, 2.5)

    # test_x_private
    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 0, 0, 1).__x)

    # test_normal_test
    def test_normal_test(self):
        x1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(x1.x, 3)

    # test_x_getter
    def test_x_getter(self):
        x2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(x2.x, 3)

    # test_x_setter
    def test_x_setter(self):
        x3 = Rectangle(1, 2, 3, 4, 5)
        x3.x = 10
        self.assertEqual(x3.x, 10)

    # test_x_None
    def test_x_None(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, None)

    # test_x_zero
    def test_x_zero(self):
        self.assertEqual(Rectangle(1, 2, 0, 4, 5).x, 0)

    # test_x_negative
    def test_x_negative(self):
        with self.assertRaises(ValueError, msg="x must be > 0"):
            Rectangle(1, 2, -1)

    # test_x_float
    def test_x_float(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, 3.5)

    # test_y_None
    def test_y_None(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, None)

    # test_y_zero
    def test_y_zero(self):
        self.assertEqual(Rectangle(1, 2, 0, 0, 5).y, 0)

    # test_y_negative
    def test_y_negative(self):
        with self.assertRaises(ValueError, msg="y must be > 0"):
            Rectangle(1, 2, -1)

    # test_y_float
    def test_y_float(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3.5)


if __name__ == "__main__":
    unittest.main()
