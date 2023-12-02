import unittest
from hello_world import hello

class HelloWorldTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), 'Hello, World!')
        
        