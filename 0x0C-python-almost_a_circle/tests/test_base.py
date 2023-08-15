#!/usr/bin/python3
"""
unittest module for the base class
"""

import json
import unittest
from models.base import Base
from os.path import isfile
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """ Test cases for the Base class """

    def setUp(self):
        """ reset number of objects to zero """
        Base.__nb_objects = 0

    def test_default_id_assignment(self):
        """
        test the default id assignment when no custom_id is provided
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id_assignment(self):
        """
        test the id assignment when a custom_id is provided
        """
        b4 = Base(12)
        b5 = Base(40)
        b6 = Base(99)

        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 40)
        self.assertEqual(b6.id, 99)

    def test_mixed_id_assignment(self):
        """
        Test the id assignment when a mixture of
        custom and default ids are used.
        """
        b7 = Base()
        b8 = Base(50)
        b9 = Base()

        self.assertEqual(b7.id, 5)
        self.assertEqual(b8.id, 50)
        self.assertEqual(b9.id, 6)

    def test_id_increment_after_custom_id(self):
        """
        Test that the id counter increments correctly
        even after a custom id is assigned.
        """
        b10 = Base(100)
        b11 = Base()

        self.assertEqual(b10.id, 100)
        self.assertEqual(b11.id, 4)

    def test_from_json_string_from_none(self):
        output = Rectangle.from_json_string(None)
        self.assertEqual([], output)

    def test_from_json_string_from_valid_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_str = Rectangle.to_json_string(list_input)
        output = Rectangle.from_json_string(json_str)
        self.assertEqual(list_input, output)

    def test_from_json_string_from_empty(self):
        output = Rectangle.from_json_string("")
        self.assertEqual([], output)

    def test_save_to_file_in_base_with_none(self):
        text = ""
        Square.save_to_file(None)
        self.assertTrue(isfile("Square.json"))
        with open("Square.json") as file:
            text = file.read()
        self.assertEqual("[]", text)

    def test_to_json_string_with_valid_dictionary(self):
        rect = Rectangle(10, 7, 2, 8, 1)
        dictionary = rect.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(sorted('[{"x": 2, "width": 10, "id": 1, "height": 7'
                                ', "y": 8}]'), sorted(json_dictionary))

    def test_mixed_data_types(self):
        """ Test with mixed data types"""
        dictionaries = [{'id': 1, 'name': 'John', 'age': 25, 'is_student': True},
                        {'id': 2, 'name': 'Jane', 'age': 30, 'is_student': False}]
        result = Base.to_json_string(dictionaries)
        expected_output = json.dumps(dictionaries)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
