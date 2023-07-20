#!/usr/bin/python3
"""
test for square class
"""


import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
from os.path import isfile


class TestRectangle(unittest.TestCase):
    def test_width_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 0, 0, 1).__width

    def test_width(self):
        w1 = Rectangle(1, 2)
        self.assertEqual(w1.width, 1)

    def test_width_None(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(None, 2)

    def test_width_zero(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 2)

    def test_width_float(self):
        self.assertRaises(TypeError, lambda: Rectangle(1.5, 2))

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 0, 0, 1).__height

    def test_height(self):
        h1 = Rectangle(1, 2)
        self.assertEqual(h1.height, 2)

    def test_height_getter(self):
        h2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(h2.height, 2)

    def test_height_setter(self):
        h3 = Rectangle(1, 2, 3, 4)
        h3.height = 10
        self.assertEqual(h3.height, 10)

    def test_height_None(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, None)

    def test_height_zero(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, 0)

    def test_height_float(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, 2.5)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 0, 0, 1).__x

    def test_x_setter(self):
        x3 = Rectangle(1, 2, 3, 4, 5)
        x3.x = 10
        self.assertEqual(x3.x, 10)

    def test_x_zero(self):
        self.assertEqual(Rectangle(1, 2, 0, 4, 5).x, 0)

    def test_x_float(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, 3.5)

    def test_y_negative(self):
        with self.assertRaises(ValueError, msg="y must be > 0"):
            Rectangle(1, 2, -1)

    def test_y_float(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3.5)

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_string_representation(self):
        """ Test __str__ method"""
        s = Square(4, 2, 3, 5)
        expected_output = "[Square] (5) 2/3 - 4"
        self.assertEqual(str(s), expected_output)

    def test_area(self):
        """ Test area method"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_with_all_args_and_all_kwargs(self):
        square = Square(10, 10, 10, 10)
        square.update(1, 1, 1, 1, id=19, size=19, x=19, y=19)
        self.assertEqual("[Square] (1) 1/1 - 1", str(square))

    def test_kwargs(self):
        r = Rectangle(width=10, height=5, x=1, y=2)
        self.assertEqual(r.id, 24)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_args_and_kwargs(self):
        r = Rectangle(2, 3, x=1, y=2)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_empty_args_and_kwargs(self):
        with self.assertRaises(TypeError):
            Rectangle(*(), **{})
    
    def test_save_to_file_with_empty_list(self):
        Square.save_to_file([])
        self.assertTrue(isfile("Square.json"))
        with open("Square.json", mode="r") as file:
            output = file.read()
            self.assertEqual("[]", output)

    def test_to_dictionary_with_only_size_specified(self):
        square = Square(10)
        actual = square.to_dictionary()
        self.assertEqual({'id': 26, 'size': 10, 'x': 0, 'y': 0}, actual)

    def test_save_to_file_with_none(self):
        text = ""
        Square.save_to_file(None)
        self.assertTrue(isfile("Square.json"))
        with open("Square.json") as file:
            text = file.read()
        self.assertEqual("[]", text)


if __name__ == "__main__":
    unittest.main()
