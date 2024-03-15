#!/usr/bin/python3
""" Module for test User class """
from datetime import datetime
from io import StringIO
from unittest.mock import patch
from models.user import User
from unittest import TestCase


class TestUserMethods(TestCase):
    """Suite to test User class"""

    def setUp(self) -> None:
        """set up method"""
        self.user = User()

    def test_user_doc(self) -> None:
        """
        Tests for the doc string
        """
        import models.user as u

        self.assertIsNotNone(u.__doc__)
        self.assertFalse(u.__doc__ == "")
        self.assertIsNotNone(self.user.__str__)
        self.assertFalse(self.user.__str__ == "")
        self.assertIsNotNone(self.user.to_dict)
        self.assertFalse(self.user.to_dict.__doc__ == "")
        self.assertIsNotNone(self.user.save)
        self.assertFalse(self.user.save.__doc__ == "")
        self.assertIsNotNone(self.user.__init__.__doc__)
        self.assertFalse(self.user.__init__.__doc__ == "")

    def test_attributes_types(self) -> None:
        """Test assigned id"""
        self.assertEqual(type(self.user.id), str)
        self.assertEqual(type(self.user.created_at), datetime)
        self.assertEqual(type(self.user.updated_at), datetime)
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)
        self.assertTrue(self.user.updated_at >= self.user.created_at)

    def test_read_from_dict(self) -> None:
        """Test read from dict"""
        my_dict = self.user.to_dict()
        self.assertEqual(type(my_dict), dict)
        output = "{"
        output += f"'id': '{self.user.id}'"
        output += f", 'created_at': '{self.user.created_at.isoformat()}'"
        output += f", 'updated_at': '{self.user.updated_at.isoformat()}'"
        output += f", '__class__': '{self.user.__class__.__name__}'"

        output += "}\n"
        with patch("sys.stdout", new=StringIO()) as out:
            print(my_dict)
            self.assertEqual(out.getvalue(), output)
        user = User(**my_dict)
        self.assertIsNot(user, self.user)
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)
        self.assertEqual(type(user.id), str)
        self.assertEqual(type(user.created_at), datetime)
        self.assertEqual(type(user.updated_at), datetime)
        self.assertEqual(user.updated_at, self.user.updated_at)
        self.assertEqual(user.created_at, self.user.created_at)
        self.assertTrue(user.updated_at >= user.created_at)

    def test_save(self):
        """ Testing save """
        self.user.save()
        key = self.user.__class__.__name__ + "." + str(self.user.id)
        from models import storage
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], self.user)

    def test_str(self):
        """ Testing str """
        self.assertEqual(str(self.user), "[User] ({}) {}".format(
            self.user.id, self.user.__dict__))
