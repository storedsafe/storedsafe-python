"""
Test that /user endpoints use the correct format.
"""
import unittest
from unittest.mock import patch
from storedsafe import StoredSafe
# pylint: disable=unused-wildcard-import,wildcard-import
from mocks import *


class User(unittest.TestCase):
    """Test /user endpoint"""

    @patch('requests.get', list_users)
    def test_list_users(self):
        """Successfully list users"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.list_users()
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', list_users_search_string)
    def test_list_users_search_string(self):
        """Successfully list users"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.list_users(search_string=MOCK_SEARCH_STRING)
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', get_user)
    def test_get_user(self):
        """Successfully get user"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.get_user(MOCK_USER_ID)
        self.assertEqual(res.status_code, 200)

    @patch('requests.post', create_user)
    def test_create_user(self):
        """Successfully create user"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.create_user(**MOCK_PARAMS)
        self.assertEqual(res.status_code, 200)

    @patch('requests.put', edit_user)
    def test_edit_user(self):
        """Successfully edit user"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.edit_user(MOCK_USER_ID, **MOCK_PARAMS)
        self.assertEqual(res.status_code, 200)

    @patch('requests.delete', delete_user)
    def test_delete_user(self):
        """Successfully delete user"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.delete_user(MOCK_USER_ID)
        self.assertEqual(res.status_code, 200)
