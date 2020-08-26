"""
/auth endpoint mocks
"""
# pylint: disable=unused-wildcard-import,wildcard-import
from .mock_response import *


def login_totp(*args, **kwargs):
    """Send mocked response for totp login."""
    data = kwargs.get('json', {})
    if is_endpoint('/api/1.0/auth', *args):
        login_type = data.get('logintype', 'yubikey')
        if login_type == 'totp':
            if (
                    data.get('username') == MOCK_USERNAME and
                    data.get('passphrase') == MOCK_PASSPHRASE and
                    data.get('otp') == MOCK_OTP
            ):
                return MOCK_LOGIN_SUCCESS
    return MOCK_ERROR


def login_yubikey(*args, **kwargs):
    """Send mocked response for yubikey login."""
    data = kwargs.get('json', {})
    if is_endpoint('/api/1.0/auth', *args):
        if (
                data.get('username') == MOCK_USERNAME and
                data.get('keys') == MOCK_PASSPHRASE + MOCK_APIKEY + MOCK_OTP
        ):
            return MOCK_LOGIN_SUCCESS
    return MOCK_ERROR


def logout(*args, **kwargs):
    """Send mocked response for logout."""
    if is_endpoint('/api/1.0/auth/logout', *args):
        if has_valid_token(**kwargs):
            return MOCK_SUCCESS
    return MOCK_ERROR


def check(*args, **kwargs):
    """Send mocked response for check."""
    if is_endpoint('/api/1.0/auth/check', *args):
        if has_valid_token(**kwargs):
            return MOCK_SUCCESS
    return MOCK_ERROR
