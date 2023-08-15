#!/usr/bin/python3
"""
unittest module for the Rectangle class
"""


import unittest
from models.rectangle import Rectangle
from os.path import isfile


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

    # test_width_setter
    def test_width_setter(self):
        w3 = Rectangle(1, 2, 3, 4)
        w3.width = 5
        self.assertEqual(w3.width, 5)

    # test_width_None
    def test_width_None(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(None, 2)

    def test_update_with_one_args_and_kwargs(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(5, width=990)
        self.assertEqual("[Rectangle] (5) 10/10 - 10/10", str(rect))

    def test_update_with_empty_args_and_one_kwargs(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update((), width=990)
        self.assertEqual("[Rectangle] (()) 10/10 - 10/10", str(rect))

    def test_id_from_valid_values_with_id(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(10, rect.id)

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

    def test_update_with_all_args_and_all_kwargs(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(1, 1, 1, 1, 1, id=19, width=19, height=19, x=19, y=19)
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(rect))

    def test_magic_str_with_valid_values(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual("[Rectangle] (10) 1/1 - 10/5", str(rect))

    def test_magic_str_without_axis_nor_id(self):
        rect = Rectangle(10, 5)
        self.assertEqual("[Rectangle] (10) 0/0 - 10/5", str(rect))

    # test_normal_test
    def test_normal_test(self):
        x1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(x1.x, 3)

    def test_save_to_file_with_none(self):
        text = ""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as file:
            text = file.read()
        self.assertEqual("[]", text)

    def test_save_to_file_with_empty_list(self):
        Rectangle.save_to_file([])
        self.assertTrue(isfile("Rectangle.json"))
        with open("Rectangle.json", mode="r") as file:
            output = file.read()
            self.assertEqual("[]", output)

    # test_x_setter
    def test_x_setter(self):
        x3 = Rectangle(1, 2, 3, 4, 5)
        x3.x = 10
        self.assertEqual(x3.x, 10)

    # test_x_None
    def test_x_None(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, None)

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

    def test_area(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(50, rect.area())

    def test_update_with_one_arg(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rect))

    def test_update_with_two_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rect))

    def test_update_with_three_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rect))


if __name__ == "__main__":
    unittest.main()
