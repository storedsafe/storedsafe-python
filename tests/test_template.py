"""
Test that /template endpoints use the correct format.
"""
import unittest
from unittest.mock import patch
from storedsafe import StoredSafe
# pylint: disable=unused-wildcard-import,wildcard-import
from mocks import *

class Template(unittest.TestCase):
    """Test /template endpoint"""

    @patch('requests.get', list_templates)
    def test_list_templates(self):
        """Successfully list templates"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.list_templates()
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', get_template)
    def test_get_template(self):
        """Successfully get template"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.get_template(MOCK_TEMPLATE_ID)
        self.assertEqual(res.status_code, 200)