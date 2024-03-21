#!/usr/bin/python3

"""
This script contains unit tests for the BaseModel class.
"""

import unittest 
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """
    
    def test_init(self):
        """
        Test initialization of BaseModel objects.
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Test saving BaseModel objects.
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at

        my_model.save()
        current_updated_at = my_model.updated_at

        self.assertNotEqual(initial_updated_at, current_updated_at)
    
    def test_to_dict(self):
        """
        Test conversion of BaseModel objects to dictionary.
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'], my_model.updated_at.isoformat())

    def test_str(self):
        """
        Test string representation of BaseModel objects.
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

if __name__ == '__main__':
    unittest.main()
