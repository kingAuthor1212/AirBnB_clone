#!/usr/bin/python3
"""test module for console.py"""
import os
import unittest
from models import storage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class TestHBNBCommand(unittest.TestCase):
    """ HBNB command interpreter test """
    def test_emptyline(self):
        HBNBCommand().onecmd("")

    def test_do_quit(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_do_EOF(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))

class TestHBNBCommand_errors(unittest.TestCase):
    """tests hbnb ccommand interpreter"""
    def test_creat_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_create_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    """shows command"""
    def test_show_missing_class(self):
        expected = "** classs name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("show")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_show_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_show_missing_id(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_show_valid_id(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("show BaseModel 121212")
            self.assertEqual(expected, obtained.getvalue().strip())

    """destroy command"""
    def test_destroy_missing_class(self):
        expected = "** classs name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_destroy_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("destroy MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_destroy_missing_id(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("destory BaseModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_destory_valid_id(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            self.assertEqual(expected, obtained.getvalue().strip())

    """all command"""
    def test_all_valid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    """update command"""
    def test_update_missing_class(self):
        expected = "** classs name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("update")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("update MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_missing_id(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_valid_id(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("update BaseModel 121212")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_missing_attribute(self):
        expected = "** attribute name missing  **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            id = obtained.getvalue().strip()
            command = "update BaseModel {}".format(id)
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_missing_value(self):
        expected = "** value missing  **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            id = obtained.getvalue().strip()
            command = "update BaseModel {} first_name".format(id)
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertEqual(expected, obtained.getvalue().strip())

class TestHBNBCommand_all_method(unittest.TestCase):
    """tests HBNB command interpreter"""

    @classmethod
    def create_all_classes(self):
        HBNBCommand().onecmd("create BasModel")
        HBNBCommand().onecmd("create User")
        HBNBCommand().onecmd("create State")
        HBNBCommand().onecmd("create City")
        HBNBCommand().onecmd("create Amenity")
        HBNBCommand().onecmd("create Place")
        HBNBCommand().onecmd("create Review")
    
    def test_all_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.create_all_classes()
        with patch("sys.stdout")