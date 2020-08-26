"""
Test that /vault endpoints use the correct format.
"""
import unittest
from unittest.mock import patch
from storedsafe import StoredSafe
# pylint: disable=unused-wildcard-import,wildcard-import
from mocks import *

class Vault(unittest.TestCase):
    """Test /vault endpoint"""

    @patch('requests.get', list_vaults)
    def test_list_vaults(self):
        """Successfully list vaults"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.list_vaults()
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', vault_objects)
    def test_vault_objects(self):
        """Successfully list objects in vault"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.vault_objects(MOCK_VAULT_ID)
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', vault_members)
    def test_vault_members(self):
        """Successfully list members in vault"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.vault_members(MOCK_VAULT_ID)
        self.assertEqual(res.status_code, 200)

    @patch('requests.post', add_vault_member)
    def test_add_vault_member(self):
        """Successful add member to vault"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.add_vault_member(MOCK_VAULT_ID, MOCK_USER_ID, MOCK_STATUS)
        self.assertEqual(res.status_code, 200)

    @patch('requests.put', edit_vault_member)
    def test_edit_vault_member(self):
        """Successful edit member in vault"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.edit_vault_member(MOCK_VAULT_ID, MOCK_USER_ID, MOCK_STATUS)
        self.assertEqual(res.status_code, 200)

    @patch('requests.delete', remove_vault_member)
    def test_remove_vault_member(self):
        """Successful remove member in vault"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.remove_vault_member(MOCK_VAULT_ID, MOCK_USER_ID)
        self.assertEqual(res.status_code, 200)

    @patch('requests.post', create_vault)
    def test_create_vault(self):
        """Successful create new vault"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.create_vault(**MOCK_PARAMS)
        self.assertEqual(res.status_code, 200)

    @patch('requests.put', edit_vault)
    def test_edit_vault(self):
        """Successful edit vault"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.edit_vault(MOCK_VAULT_ID, **MOCK_PARAMS)
        self.assertEqual(res.status_code, 200)

    @patch('requests.delete', delete_vault)
    def test_delete_vault(self):
        """Successful delete vault"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.delete_vault(MOCK_VAULT_ID)
        self.assertEqual(res.status_code, 200)
