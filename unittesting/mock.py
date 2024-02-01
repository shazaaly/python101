#!/usr/bin/env python3

import unittest
from unittest import mock
from unittest.mock import patch
from urllib import request
import req


class TestGetJson(unittest.TestCase):
    @patch('req.requests.get')
    def testGetJson(self, mock_get):  # Accept the mock object as an argument
        test_cases = [
            ("https://shazaali.substack.com", {"payload": True}) 
        ]
        
        for t_url, t_payload in test_cases:
            # configure the mock to return a mock response object with a .json() method that returns t_payload
            mock_get.return_value.json.return_value = t_payload
            res = req.get_json(t_url)
            self.assertEqual(res, t_payload)  # Assert that the result matches the expected payload
        # Verify requests.get was called with the test URL.
            mock_get.assert_called_with(t_url)

            # Reset the mock for the next iteration.
            mock_get.reset_mock()

if __name__ == '__main__':
    unittest.main()
