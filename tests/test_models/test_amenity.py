#!/usr/bin/python3
""" Module for test Amenity class """
from datetime import datetime
from io import StringIO
from unittest.mock import patch
from models.amenity import Amenity
from unittest import TestCase


class TestAmenityMethods(TestCase):
    """Suite to test Amenity class"""

    def setUp(self) -> None:
        """set up method"""
        self.amenity = Amenity()

    def test_amenity_doc(self) -> None:
        """
        Tests for the doc string
        """
        import models.amenity as a

        self.assertIsNotNone(a.__doc__)
        self.assertFalse(a.__doc__ == "")
        self.assertIsNotNone(self.amenity.__str__)
        self.assertFalse(self.amenity.__str__ == "")
        self.assertIsNotNone(self.amenity.to_dict)
        self.assertFalse(self.amenity.to_dict.__doc__ == "")
        self.assertIsNotNone(self.amenity.save)
        self.assertFalse(self.amenity.save.__doc__ == "")
        self.assertIsNotNone(self.amenity.__init__.__doc__)
        self.assertFalse(self.amenity.__init__.__doc__ == "")

    def test_attributes_types(self) -> None:
        """Test assigned id"""
        self.assertEqual(type(self.amenity.id), str)
        self.assertEqual(type(self.amenity.created_at), datetime)
        self.assertEqual(type(self.amenity.updated_at), datetime)
        self.assertEqual(type(self.amenity.name), str)
        self.assertTrue(self.amenity.updated_at >= self.amenity.created_at)

    def test_read_from_dict(self) -> None:
        """Test read from dict"""
        my_dict = self.amenity.to_dict()
        self.assertEqual(type(my_dict), dict)
        output = "{"
        output += f"'id': '{self.amenity.id}'"
        output += f", 'created_at': '{self.amenity.created_at.isoformat()}'"
        output += f", 'updated_at': '{self.amenity.updated_at.isoformat()}'"
        output += f", '__class__': '{self.amenity.__class__.__name__}'"
        output += "}\n"
        with patch("sys.stdout", new=StringIO()) as out:
            print(my_dict)
            self.assertEqual(out.getvalue(), output)
        amenity = Amenity(**my_dict)
        self.assertIsNot(amenity, self.amenity)
        self.assertEqual(type(amenity.name), str)
        self.assertEqual(type(amenity.id), str)
        self.assertEqual(type(amenity.created_at), datetime)
        self.assertEqual(type(amenity.updated_at), datetime)
        self.assertTrue(amenity.updated_at >= amenity.created_at)

    def test_save(self):
        """ Testing save """
        self.amenity.save()
        key = self.amenity.__class__.__name__ + "." + self.amenity.id
        from models import storage
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], self.amenity)

    def test_str(self):
        """ Testing str """
        self.assertEqual(str(self.amenity), "[Amenity] ({}) {}".
                         format(self.amenity.id, self.amenity.__dict__))
