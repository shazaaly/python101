#!/usr/bin/env python3

import unittest
from add_function import add_numbers

class testAddNumbers(unittest.TestCase):
    """ testing add numbers """
    
    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)

if __name__ == "__main__":
    unittest.main()