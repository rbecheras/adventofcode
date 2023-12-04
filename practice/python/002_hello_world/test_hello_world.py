"""Just a hello world test"""
import unittest
from hello_world import hello


class HelloWorldTest(unittest.TestCase):
    """Test the hello function"""

    def test_hello(self):
        """Test the hello function"""
        self.assertEqual(hello(), "Hello, World!")
