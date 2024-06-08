#!/usr/bin/python3
"""Test script for testing the HBNBCommand Class"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models import storage

class TestHBNBCommand(unittest.TestCase):
    """Test the HBNBCommand Console"""

    def setUp(self):
        """Set up the test environment"""
        storage.reset()  # Assuming you have a reset method to clear storage
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after each test"""
        storage.reset()  # Reset storage again to ensure clean state

    def test_help(self):
        """Tests the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
        expected_output = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update\n
"""
        self.assertEqual(expected_output, f.getvalue())

    def test_do_quit(self):
        """Tests the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
        self.assertEqual("", f.getvalue())

    def test_do_EOF(self):
        """Tests the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("EOF")
        self.assertEqual("\n", f.getvalue())

    def test_emptyline(self):
        """Tests the emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
        self.assertEqual("", f.getvalue())

    def test_create(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
        output = f.getvalue().strip()
        self.assertTrue(len(output) == 36)  # UUID length

    def test_show(self):
        """Test the show command"""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {model.id}")
        self.assertIn(model.id, f.getvalue())

    def test_destroy(self):
        """Test the destroy command"""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {model.id}")
        self.assertNotIn(model.id, storage.all())

    def test_all(self):
        """Test the all command"""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
        self.assertIn(str(model), f.getvalue())

    def test_update(self):
        """Test the update command"""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {model.id} name 'My Model'")
        self.assertEqual(storage.all()[f"BaseModel.{model.id}"].name, "My Model")

    def test_count(self):
        """Test the count command"""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
        self.assertEqual("1\n", f.getvalue())

if __name__ == "__main__":
    unittest.main()
