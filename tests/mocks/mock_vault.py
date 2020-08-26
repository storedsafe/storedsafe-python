"""
/vault endpoint mocks
"""
# pylint: disable=unused-wildcard-import,wildcard-import
from .mock_response import *


def list_vaults(*args, **kwargs):
    """Send mocked response for listing vaults."""
    if is_endpoint('/api/1.0/vault', *args):
        if has_valid_token(**kwargs):
            return MOCK_SUCCESS
    return MOCK_ERROR


def vault_objects(*args, **kwargs):
    """Send mocked response for listing vault objects."""
    if is_endpoint(f'/api/1.0/vault/{MOCK_VAULT_ID}', *args):
        if has_valid_token(**kwargs):
            return MOCK_SUCCESS
    return MOCK_ERROR


def vault_members(*args, **kwargs):
    """Send mocked response for listing vault objects."""
    if is_endpoint(f'/api/1.0/vault/{MOCK_VAULT_ID}/members', *args):
        if has_valid_token(**kwargs):
            return MOCK_SUCCESS
    return MOCK_ERROR


def add_vault_member(*args, **kwargs):
    """Send mocked response for adding a member to a vault."""
    data = kwargs.get('json', {})
    if is_endpoint(f'/api/1.0/vault/{MOCK_VAULT_ID}/member/{MOCK_USER_ID}', *args):
        if has_valid_token(**kwargs) and data.get('status') == MOCK_STATUS:
            return MOCK_SUCCESS
    return MOCK_ERROR


def edit_vault_member(*args, **kwargs):
    """Send mocked response for editing a member in a vault."""
    data = kwargs.get('json', {})
    if is_endpoint(f'/api/1.0/vault/{MOCK_VAULT_ID}/member/{MOCK_USER_ID}', *args):
        if has_valid_token(**kwargs) and data.get('status') == MOCK_STATUS:
            return MOCK_SUCCESS
    return MOCK_ERROR


def remove_vault_member(*args, **kwargs):
    """Send mocked response for removing a member from a vault."""
    if is_endpoint(f'/api/1.0/vault/{MOCK_VAULT_ID}/member/{MOCK_USER_ID}', *args):
        if has_valid_token(**kwargs):
            return MOCK_SUCCESS
    return MOCK_ERROR


def create_vault(*args, **kwargs):
    """Send mocked response for creating a vault."""
    data = kwargs.get('json', {})
    if is_endpoint('/api/1.0/vault', *args):
        if has_valid_token(**kwargs) and data == MOCK_PARAMS:
            return MOCK_SUCCESS
    return MOCK_ERROR


def edit_vault(*args, **kwargs):
    """Send mocked response for editing a vault."""
    data = kwargs.get('json', {})
    if is_endpoint(f'/api/1.0/vault/{MOCK_VAULT_ID}', *args):
        if has_valid_token(**kwargs) and data == MOCK_PARAMS:
            return MOCK_SUCCESS
    return MOCK_ERROR


def delete_vault(*args, **kwargs):
    """Send mocked response for deleting a vault."""
    if is_endpoint(f'/api/1.0/vault/{MOCK_VAULT_ID}', *args):
        if has_valid_token(**kwargs):
            return MOCK_SUCCESS
    return MOCK_ERROR
