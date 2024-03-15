#!/usr/bin/python3
""" Module for test State class """
from datetime import datetime
from io import StringIO
from unittest.mock import patch
from models.state import State
from unittest import TestCase


class TestStateMethods(TestCase):
    """Suite to test State class"""

    def setUp(self) -> None:
        """set up method"""
        self.state = State()

    def test_state_doc(self) -> None:
        """
        Tests for the doc string
        """
        import models.state as s

        self.assertIsNotNone(s.__doc__)
        self.assertFalse(s.__doc__ == "")
        self.assertIsNotNone(self.state.__str__)
        self.assertFalse(self.state.__str__ == "")
        self.assertIsNotNone(self.state.to_dict)
        self.assertFalse(self.state.to_dict.__doc__ == "")
        self.assertIsNotNone(self.state.save)
        self.assertFalse(self.state.save.__doc__ == "")
        self.assertIsNotNone(self.state.__init__.__doc__)
        self.assertFalse(self.state.__init__.__doc__ == "")

    def test_attributes_types(self) -> None:
        """Test assigned id"""
        self.assertEqual(type(self.state.id), str)
        self.assertEqual(type(self.state.created_at), datetime)
        self.assertEqual(type(self.state.updated_at), datetime)
        self.assertEqual(type(self.state.name), str)
        self.assertTrue(self.state.updated_at >= self.state.created_at)

    def test_read_from_dict(self) -> None:
        """Test read from dict"""
        my_dict = self.state.to_dict()
        self.assertEqual(type(my_dict), dict)
        output = "{"
        output += f"'id': '{self.state.id}'"
        output += f", 'created_at': '{self.state.created_at.isoformat()}'"
        output += f", 'updated_at': '{self.state.updated_at.isoformat()}'"
        output += f", '__class__': '{self.state.__class__.__name__}'"
        output += "}\n"
        with patch("sys.stdout", new=StringIO()) as out:
            print(my_dict)
            self.assertEqual(out.getvalue(), output)
        state = State(**my_dict)
        self.assertIsNot(state, self.state)
        self.assertEqual(type(state.name), str)
        self.assertEqual(type(state.id), str)
        self.assertEqual(type(state.created_at), datetime)
        self.assertEqual(type(state.updated_at), datetime)
        self.assertTrue(state.updated_at >= state.created_at)

    def test_save(self):
        """ Testing save """
        self.state.save()
        key = self.state.__class__.__name__ + "." + str(self.state.id)
        from models import storage
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], self.state)

    def test_str(self):
        """ Testing str """
        self.assertEqual(str(self.state), "[State] ({}) {}".
                         format(self.state.id, self.state.__dict__))
