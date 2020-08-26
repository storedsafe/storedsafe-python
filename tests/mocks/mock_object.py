"""
/object endpoint mocks
"""
# pylint: disable=unused-wildcard-import,wildcard-import
from .mock_response import *


def get_object(*args, **kwargs):
    """Send mocked response getting object."""
    if is_endpoint(f'/api/1.0/object/{MOCK_OBJECT_ID}', *args):
        if has_valid_token(**kwargs):
            return MOCK_SUCCESS
    return MOCK_ERROR


def get_object_children(*args, **kwargs):
    """Send mocked response getting object."""
    data = kwargs.get('params', {})
    if is_endpoint(f'/api/1.0/object/{MOCK_OBJECT_ID}', *args):
        if has_valid_token(**kwargs) and data.get('children') == 'true':
            return MOCK_SUCCESS
    return MOCK_ERROR


def decrypt_object(*args, **kwargs):
    """Send mocked response for decrypting object."""
    data = kwargs.get('params', {})
    if is_endpoint(f'/api/1.0/object/{MOCK_OBJECT_ID}', *args):
        if has_valid_token(**kwargs) and data.get('decrypt') == 'true':
            return MOCK_SUCCESS
    return MOCK_ERROR


def get_file(*args, **kwargs):
    """Send mocked response for getting file."""
    data = kwargs.get('params', {})
    if is_endpoint(f'/api/1.0/object/{MOCK_OBJECT_ID}', *args):
        if has_valid_token(**kwargs) and data.get('decrypt') == 'true' and data.get('filedata') == 'true':
            return MOCK_SUCCESS
    return MOCK_ERROR


def create_object(*args, **kwargs):
    """Send mocked response for creating an object."""
    data = kwargs.get('json', {})
    if is_endpoint('/api/1.0/object', *args):
        if has_valid_token(**kwargs) and data == MOCK_PARAMS:
            return MOCK_SUCCESS
    return MOCK_ERROR


def edit_object(*args, **kwargs):
    """Send mocked response for editing an object."""
    data = kwargs.get('json', {})
    if is_endpoint(f'/api/1.0/object/{MOCK_OBJECT_ID}', *args):
        if has_valid_token(**kwargs) and data == MOCK_PARAMS:
            return MOCK_SUCCESS
    return MOCK_ERROR


def delete_object(*args, **kwargs):
    """Send mocked response for deleting an object."""
    if is_endpoint(f'/api/1.0/object/{MOCK_OBJECT_ID}', *args):
        if has_valid_token(**kwargs):
            return MOCK_SUCCESS
    return MOCK_ERROR


def find(*args, **kwargs):
    """Send mocked response for finding objects."""
    data = kwargs.get('params', {})
    if is_endpoint(f'/api/1.0/find', *args):
        if has_valid_token(**kwargs) and data.get('needle') == MOCK_NEEDLE:
            return MOCK_SUCCESS
    return MOCK_ERROR
