"""
Test that /object endpoints use the correct format.
"""
import unittest
from unittest.mock import patch
from storedsafe import StoredSafe
# pylint: disable=unused-wildcard-import,wildcard-import
from mocks import *

class Object(unittest.TestCase):
    """Test /object endpoint"""

    @patch('requests.get', get_object)
    def test_get_object(self):
        """Successfully get object"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.get_object(MOCK_OBJECT_ID)
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', get_object_children)
    def test_get_object_children(self):
        """Successfully get object with children"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.get_object(MOCK_OBJECT_ID, children=True)
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', decrypt_object)
    def test_decrypt_object(self):
        """Successfully decrypt object"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.decrypt_object(MOCK_OBJECT_ID)
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', get_file)
    def test_get_file(self):
        """Successfully get file"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.get_file(MOCK_OBJECT_ID)
        self.assertEqual(res.status_code, 200)

    @patch('requests.post', create_object)
    def test_create_object(self):
        """Successful create object"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.create_object(**MOCK_PARAMS)
        self.assertEqual(res.status_code, 200)

    @patch('requests.put', edit_object)
    def test_edit_object(self):
        """Successful edit object"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.edit_object(MOCK_OBJECT_ID, **MOCK_PARAMS)
        self.assertEqual(res.status_code, 200)

    @patch('requests.delete', delete_object)
    def test_delete_object(self):
        """Successful delete object"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.delete_object(MOCK_OBJECT_ID)
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', find)
    def test_find(self):
        """Successfully request find"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.find(MOCK_NEEDLE)
        self.assertEqual(res.status_code, 200)
