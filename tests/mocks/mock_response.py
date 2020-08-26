"""
Define mocked responses mimicking the StoredSafe REST-like API.

Because the wrapper is transparent, the only required return data
is the token on login requests and the HTTP status to indicate whether
the request was correct or not.
"""
MOCK_HOST = "test.storedsafe.com"
MOCK_URL = f"https://{MOCK_HOST}"
MOCK_TOKEN = "mock-token"
MOCK_APIKEY = "mock-api-key"
MOCK_USERNAME = "mock-username"
MOCK_PASSPHRASE = "mock-passphrase"
MOCK_OTP = "mock-otp"

MOCK_VAULT_ID = 42
MOCK_OBJECT_ID = 93
MOCK_TEMPLATE_ID = 10
MOCK_USER_ID = 18
MOCK_STATUS = 2
MOCK_NEEDLE = 'Waldo'
MOCK_SEARCH_STRING = 'Nilsson'

MOCK_PARAMS = {'first': 1, 'second': 'two', 'third': True}


class MockResponse:
    """
    Mimicks a minimal StoredSafe response as presented by the
    requests library.
    """

    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        """Returns the JSON data of the response."""
        return self.json_data


MOCK_ERROR = MockResponse({}, 403)
MOCK_LOGIN_SUCCESS = MockResponse({'CALLINFO': {'token': MOCK_TOKEN}}, 200)
MOCK_SUCCESS = MockResponse({}, 200)


def is_endpoint(endpoint, *args):
    """Check if the intended enpoint matches the URL"""
    return args[0] == MOCK_URL + endpoint


def has_valid_token(**kwargs):
    """Check if a valid token exists in the header"""
    headers = kwargs.get('headers', {})
    return headers.get('X-Http-Token') == MOCK_TOKEN
