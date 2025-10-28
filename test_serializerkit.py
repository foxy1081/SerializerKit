# test_serializerkit.py
"""
Tests for SerializerKit module.
"""

import unittest
from serializerkit import SerializerKit

class TestSerializerKit(unittest.TestCase):
    """Test cases for SerializerKit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SerializerKit()
        self.assertIsInstance(instance, SerializerKit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SerializerKit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
