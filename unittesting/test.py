#!/usr/bin/env python3

import unittest
from access_nested_map import access_nested_map
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({'a': {'b': 1}}, ('a', 'b'), 1),
    ])
    def test_access_nested_map_valid(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({'a': {'b': 1}}, ('a', 'c')),
    ])
    def test_access_nested_map_key_error(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

# This allows the tests to be run from the command line
if __name__ == '__main__':
    unittest.main()
