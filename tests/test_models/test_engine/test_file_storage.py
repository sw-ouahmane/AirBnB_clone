#!/usr/bin/python3
""" Module for test storage """
from io import StringIO
from unittest.mock import patch
from unittest import TestCase
from models.engine.file_storage import FileStorage
from models import BaseModel


class TestBaseMethods(TestCase):
    """Suite to test storage"""

    def setUp(self) -> None:
        """set up method for FileStorage"""
        self.storage = FileStorage()

    def test_attributes(self):
        """Test if file.json content is a dictionary"""
        self.assertEqual(self.storage.file_path, "file.json")
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """Test all methods"""
        model = BaseModel()
        self.storage.new(model)
        identifier = f"BaseModel.{model.id}"
        self.assertIn(identifier, self.storage.all().keys())
