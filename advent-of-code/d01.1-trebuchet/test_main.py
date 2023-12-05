"""Test the main function"""
import unittest
import os
import main


class TestMain(unittest.TestCase):
    """Test the main function"""

    def test_read_file(self):
        """Test the read_file function"""
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, "test_input.txt")
        content = main.read_file(file_path)
        expected = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"
        self.assertEqual(content, expected)

    def test_calibrate(self):
        """Test the calibrate function"""
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, "test_input.txt")
        content = main.read_file(file_path)
        expected = 142
        self.assertEqual(main.calibrate(content), expected)
