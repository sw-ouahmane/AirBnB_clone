#!/usr/bin/python3
""" Module for test Place class """
from datetime import datetime
from io import StringIO
from unittest.mock import patch
from models.place import Place
from unittest import TestCase


class TestPlaceMethods(TestCase):
    """Suite to test Place class"""

    def setUp(self) -> None:
        """set up method"""
        self.place = Place()

    def test_place_doc(self) -> None:
        """
        Tests for the doc string
        """
        import models.place as p

        self.assertIsNotNone(p.__doc__)
        self.assertFalse(p.__doc__ == "")
        self.assertIsNotNone(self.place.__str__)
        self.assertFalse(self.place.__str__ == "")
        self.assertIsNotNone(self.place.to_dict)
        self.assertFalse(self.place.to_dict.__doc__ == "")
        self.assertIsNotNone(self.place.save)
        self.assertFalse(self.place.save.__doc__ == "")
        self.assertIsNotNone(self.place.__init__.__doc__)
        self.assertFalse(self.place.__init__.__doc__ == "")

    def test_attributes_types(self) -> None:
        """Test assigned id"""
        self.assertEqual(type(self.place.id), str)
        self.assertEqual(type(self.place.created_at), datetime)
        self.assertEqual(type(self.place.updated_at), datetime)
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)
        self.assertTrue(self.place.updated_at >= self.place.created_at)

    def test_read_from_dict(self) -> None:
        """Test read from dict"""
        my_dict = self.place.to_dict()
        self.assertEqual(type(my_dict), dict)
        output = "{"
        output += f"'id': '{self.place.id}'"
        output += f", 'created_at': '{self.place.created_at.isoformat()}'"
        output += f", 'updated_at': '{self.place.updated_at.isoformat()}'"
        output += f", '__class__': '{self.place.__class__.__name__}'"
        output += "}\n"
        with patch("sys.stdout", new=StringIO()) as out:
            print(my_dict)
            self.assertEqual(out.getvalue(), output)
        place = Place(**my_dict)
        self.assertIsNot(place, self.place)
        self.assertEqual(type(place.city_id), str)
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(type(place.name), str)
        self.assertEqual(type(place.description), str)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(type(place.id), str)
        self.assertEqual(type(place.created_at), datetime)
        self.assertEqual(type(place.updated_at), datetime)
        self.assertTrue(place.updated_at >= place.created_at)

    def test_save(self):
        """ Testing save """
        self.place.save()
        key = self.place.__class__.__name__ + "." + self.place.id
        from models import storage
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], self.place)

    def test_str(self):
        """ Testing str """
        self.assertEqual(str(self.place),
                         f"[Place] ({self.place.id}) {self.place.__dict__}")
