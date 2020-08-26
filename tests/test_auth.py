"""
Test that /auth endpoints use the correct format.
"""
import unittest
from unittest.mock import patch
from storedsafe import StoredSafe
# pylint: disable=unused-wildcard-import,wildcard-import
from mocks import *

class Auth(unittest.TestCase):
    """Test /auth endpoint"""

    @patch('requests.post', login_totp)
    def test_login_totp(self):
        """Successful login using TOTP"""
        api = StoredSafe(host=MOCK_HOST, apikey=MOCK_APIKEY)
        res = api.login_totp(MOCK_USERNAME, MOCK_PASSPHRASE, MOCK_OTP)

        self.assertEqual(api.token, MOCK_TOKEN)
        self.assertEqual(res.status_code, 200)

    @patch('requests.post', login_yubikey)
    def test_login_yubikey(self):
        """Successful login using TOTP"""
        api = StoredSafe(host=MOCK_HOST, apikey=MOCK_APIKEY)
        res = api.login_yubikey(MOCK_USERNAME, MOCK_PASSPHRASE, MOCK_OTP)

        self.assertEqual(api.token, MOCK_TOKEN)
        self.assertEqual(res.status_code, 200)

    @patch('requests.get', logout)
    def test_logout(self):
        """Successful logout"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.logout()
        self.assertEqual(res.status_code, 200)

    @patch('requests.post', check)
    def test_check(self):
        """Successful check"""
        api = StoredSafe(host=MOCK_HOST, token=MOCK_TOKEN)
        res = api.check()
        self.assertEqual(res.status_code, 200)
