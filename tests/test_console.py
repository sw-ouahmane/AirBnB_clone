import uuid
import os
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
import console


class TestConsole(unittest.TestCase):
    def setUp(self):
        """ Create file at the beginning of every test"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Delete created file after every test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_help(self) -> None:
        """Test help command"""
        commands = ["show", "create", "all", "update", "destroy", "count"]
        for command in commands:
            output = f" {command} command \n"
            with patch("sys.stdout", new=StringIO()) as out:
                HBNBCommand().onecmd(f"help {command}")
                self.assertEqual(out.getvalue(), output)
        output = ""
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("quit")
            self.assertEqual(out.getvalue(), output)

        for command in commands:
            with patch("sys.stdout", new=StringIO()) as f:
                HBNBCommand().onecmd(f"help {command}")
                output = f.getvalue().strip()
                self.assertIsNotNone(output)

    def test_error_messages(self) -> None:
        """Test that error messages are displayed
        for invalid commands and arguments."""
        output = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("show")
            self.assertEqual(out.getvalue(), output)

        output = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("create")
            self.assertEqual(out.getvalue(), output)

        output = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("update")
            self.assertEqual(out.getvalue(), output)

        output = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(out.getvalue(), output)

        output = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("create my_class")
            self.assertEqual(out.getvalue(), output)

        output = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("show my_class")
            self.assertEqual(out.getvalue(), output)

        output = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("destroy my_class")
            self.assertEqual(out.getvalue(), output)

        output = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("update my_class")
            self.assertEqual(out.getvalue(), output)

        output = "** instance id missing **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("show User")
            self.assertEqual(out.getvalue(), output)

        output = "** instance id missing **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("update User")
            self.assertEqual(out.getvalue(), output)

    def test_docs(self) -> None:
        """Test that all methods in the console module
        and HBNBCommand class have docstrings."""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.__doc__)
        methods = [
            HBNBCommand.do_EOF,
            HBNBCommand.do_exit,
            HBNBCommand.do_quit,
            HBNBCommand.do_create,
            HBNBCommand.do_show,
            HBNBCommand.do_destroy,
            HBNBCommand.do_all,
            HBNBCommand.do_update,
            HBNBCommand.default
        ]
        for method in methods:
            self.assertIsNotNone(method.__doc__)

    def test_quit(self) -> None:
        """Test that the quit, EOF, and exit commands exit the console."""
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("quit")
            self.assertEqual(out.getvalue().strip(), "")

        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(out.getvalue().strip(), "")

        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("exit")
            self.assertEqual(out.getvalue().strip(), "")

    def test_empty_line(self) -> None:
        """Test that the empty line command does not produce any output."""
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("")
            self.assertEqual(out.getvalue().strip(), "")

    def test_create(self) -> None:
        """Test that the create command creates
        instances of the specified classes."""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update(self) -> None:
        """Test that the update command updates
        instances of the specified classes."""
        obj = User()
        obj.save()
        cmd = f"update User {obj.id} __class__ 'not allowed'"
        self.assertNotEqual(obj.__class__, "not allowed")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

        obj = User()
        obj.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {obj.id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

        obj = User()
        obj.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {obj.id} name")
            output = f.getvalue().strip()
            self.assertEqual(output, "** value missing **")

        obj = User()
        obj.save()
        cmd1 = f"update User {obj.id} name 'malibu smith' "
        cmd2 = f"age 30 height 1.7"
        HBNBCommand().onecmd(cmd1 + cmd2)
        self.assertFalse(hasattr(obj, "age"))
        self.assertFalse(hasattr(obj, "height"))

    def test_all(self) -> None:
        """Test that the all command lists all
        instances of the specified classes."""
        obj1 = User()
        obj1.save()
        obj2 = User()
        obj2.save()
        obj2.save()
        obj4 = Place()
        obj4.save()
        obj5 = Place()
        obj5.save()

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({obj1.id})", output)
            self.assertIn(f"[User] ({obj2.id})", output)
            self.assertNotIn(f"[Place]", output)
            self.assertNotIn(f"[Basemodel]", output)
            self.assertNotIn(f"[City]", output)
            self.assertTrue(output.startswith('["'))
            self.assertTrue(output.endswith('"]'))

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("model.all()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        obj1 = User()
        obj1.save()
        obj2 = User()
        obj2.save()
        obj2.save()
        obj4 = Place()
        obj4.save()
        obj5 = Place()
        obj5.save()

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({obj1.id})", output)
            self.assertIn(f"[User] ({obj2.id})", output)
            self.assertNotIn(f"[Place]", output)
            self.assertNotIn(f"[Basemodel]", output)
            self.assertNotIn(f"[City]", output)
            self.assertTrue(output.startswith('["'))
            self.assertTrue(output.endswith('"]'))

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_count(self) -> None:
        """Test that the count command returns the number
        of instances of the specified classes."""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "0")

        obj = User()
        obj.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "1")

        obj = User()
        obj.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "0")

        obj = User()
        obj.save()
        obj = Place()
        obj.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "1")

    def test_show(self) -> None:
        """Test that the show command displays information
        about the specified instance."""
        obj = User()
        obj.save()
        cmd = f"User.show({obj.id})"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({obj.id})", output)
            self.assertIn("created_at", output)
            self.assertIn("updated_at", output)
            self.assertIn("id", output)
            self.assertNotIn("__class__", output)
            self.assertFalse(output.startswith('["'))
            self.assertFalse(output.endswith('"]'))

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.show()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.show(121212)")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy(self) -> None:
        """Test that the destroy command deletes the specified instance."""
        obj = User()
        obj.save()
        cmd = f"User.destroy({obj.id})"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            HBNBCommand().onecmd(f"show User {obj.id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.destroy()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(121212)")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

        obj = User()
        obj.save()
        cmd = f"destroy User {obj.id}"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            HBNBCommand().onecmd(f"show User {obj.id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    #     cmd = f"Review.update({test_inst.id}, {attr_dict})"
