#!/usr/bin/python3
""" Module for test City class """
from datetime import datetime
from io import StringIO
from unittest.mock import patch
from models.city import City
from unittest import TestCase


class TestCityMethods(TestCase):
    """Suite to test City class"""

    def setUp(self) -> None:
        """set up method"""
        self.city = City()

    def test_city_doc(self) -> None:
        """
        Tests for the doc string
        """
        import models.city as c

        self.assertIsNotNone(c.__doc__)
        self.assertFalse(c.__doc__ == "")
        self.assertIsNotNone(self.city.__str__)
        self.assertFalse(self.city.__str__ == "")
        self.assertIsNotNone(self.city.to_dict)
        self.assertFalse(self.city.to_dict.__doc__ == "")
        self.assertIsNotNone(self.city.save)
        self.assertFalse(self.city.save.__doc__ == "")
        self.assertIsNotNone(self.city.__init__.__doc__)
        self.assertFalse(self.city.__init__.__doc__ == "")

    def test_attributes_types(self) -> None:
        """Test assigned id"""
        self.assertEqual(type(self.city.id), str)
        self.assertEqual(type(self.city.created_at), datetime)
        self.assertEqual(type(self.city.updated_at), datetime)
        self.assertEqual(type(self.city.state_id), str)
        self.assertEqual(type(self.city.name), str)
        self.assertTrue(self.city.updated_at >= self.city.created_at)

    def test_read_from_dict(self) -> None:
        """Test read from dict"""
        my_dict = self.city.to_dict()
        self.assertEqual(type(my_dict), dict)
        output = "{"
        output += f"'id': '{self.city.id}'"
        output += f", 'created_at': '{self.city.created_at.isoformat()}'"
        output += f", 'updated_at': '{self.city.updated_at.isoformat()}'"
        output += f", '__class__': '{self.city.__class__.__name__}'"
        output += "}\n"
        with patch("sys.stdout", new=StringIO()) as out:
            print(my_dict)
            self.assertEqual(out.getvalue(), output)
        city = City(**my_dict)
        self.assertIsNot(city, self.city)
        self.assertEqual(type(city.state_id), str)
        self.assertEqual(type(city.name), str)
        self.assertEqual(type(city.id), str)
        self.assertEqual(type(city.created_at), datetime)
        self.assertEqual(type(city.updated_at), datetime)

    def test_save(self):
        """ Testing save """
        self.city.save()
        key = self.city.__class__.__name__ + "." + str(self.city.id)
        from models import storage
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], self.city)

    def test_str(self):
        """ Testing str """
        self.assertEqual(str(self.city), "[City] ({}) {}".
                         format(self.city.id, self.city.__dict__))
