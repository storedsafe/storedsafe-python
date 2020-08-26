"""
/object endpoint mocks
"""
# pylint: disable=unused-wildcard-import,wildcard-import
from .mock_response import *


def status_values(*args, **kwargs):
    """Send mocked response listing status values."""
    if is_endpoint('/api/1.0/utils/statusvalues', *args):
        if has_valid_token(**kwargs):
            return MOCK_SUCCESS
    return MOCK_ERROR


def password_policies(*args, **kwargs):
    """Send mocked response listing password policies."""
    if is_endpoint('/api/1.0/utils/policies', *args):
        if has_valid_token(**kwargs):
            return MOCK_SUCCESS
    return MOCK_ERROR


def version(*args, **kwargs):
    """Send mocked response getting StoredSafe version."""
    if is_endpoint('/api/1.0/utils/version', *args):
        if has_valid_token(**kwargs):
            return MOCK_SUCCESS
    return MOCK_ERROR

def generate_password(*args, **kwargs):
    """Send mocked response generating password."""
    if is_endpoint('/api/1.0/utils/pwgen', *args):
        if has_valid_token(**kwargs):
            return MOCK_SUCCESS
    return MOCK_ERROR

def generate_password_params(*args, **kwargs):
    """Send mocked response generating password with parameters."""
    data = kwargs.get('params', {})
    if is_endpoint('/api/1.0/utils/pwgen', *args):
        if has_valid_token(**kwargs) and data == MOCK_PARAMS:
            return MOCK_SUCCESS
    return MOCK_ERROR
