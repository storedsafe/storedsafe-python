"""
Test that /utils endpoints use the correct format.
"""
import unittest
from unittest.mock import patch
from storedsafe import StoredSafe
# pylint: disable=unused-wildcard-import,wildcard-import
from mocks import *


class Utils(unittest.TestCase):
    """Test /utils endpoint"""

    @patch('requests.get', status_values)
    def test_status_values(self):
        """Successfully list status values"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.status_values()
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', password_policies)
    def test_password_policies(self):
        """Successfully list password policies"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.password_policies()
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', version)
    def test_version(self):
        """Successfully get StoredSafe version"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.version()
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', generate_password)
    def test_generate_password(self):
        """Successfully generate password"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.generate_password()
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', generate_password_params)
    def test_generate_password_params(self):
        """Successfully generate password with parameters"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.generate_password(**MOCK_PARAMS)
        self.assertEqual(res.status_code, 200)
