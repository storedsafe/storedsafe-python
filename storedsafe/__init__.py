import requests

class TokenUndefinedException(Exception):
    pass

class StoredSafe:
    def __init__(self, host, apikey, token=None):
        self.host = host
        self.apikey = apikey
        self.token = token

    ###
    # Helper functions.
    ##
    def __auth(self, data):
        """Authenticate with StoredSafe and save token if the request was successful."""
        r = requests.post(self.__get_url('/auth'), json=data)
        if r.status_code == 200:
            data = r.json()
            self.token = data['CALLINFO']['token']
        return r

    def __headers(self):
        """Create the required headers for requests to the StoredSafe API."""
        self.__assert_token_exists()
        return { 'X-Http-Token': self.token }

    def __assert_token_exists(self):
        """Throws TokenUndefinedException if token is None."""
        if self.token is None:
            raise TokenUndefinedException()

    def __get_url(self, path):
        """Get the full url of the relative API path."""
        return f'https://{self.host}/api/1.0{path}'

    def __get(self, path, params=None):
        """Send a GET request to the provided relative API path."""
        self.__assert_token_exists()
        return requests.get(self.__get_url(path), params=params, headers=self.__headers())

    def __post(self, path, data):
        """Send a POST request to the provided relative API path."""
        self.__assert_token_exists()
        return requests.post(self.__get_url(path), json=data, headers=self.__headers())

    def __put(self, path, data):
        """Send a PUT request to the provided relative API path."""
        self.__assert_token_exists()
        return requests.put(self.__get_url(path), json=data, headers=self.__headers())

    def __delete(self, path):
        """Send a DELETE request to the provided relative API path."""
        self.__assert_token_exists()
        return requests.delete(self.__get_url(path), headers=self.__headers())

    ###
    # API Auth functions.
    ##
    def login_totp(self, username, passphrase, otp):
        """Request login using TOTP."""
        data = {
            'username': username,
            'passphrase': passphrase,
            'otp': otp,
            'apikey': self.apikey,
            'logintype': 'totp',
        }
        return self.__auth(data)

    def login_yubikey(self, username, passphrase, otp):
        """Request login using Yubico OTP."""
        data = {
            'username': username,
            'keys': f'{passphrase}{self.apikey}{otp}',
            'apikey': self.apikey,
        }
        return self.__auth(data)

    def logout(self):
        """Request logout."""
        return self.__get('/auth/logout')

    def check(self):
        """Request check status of session."""
        return self.__post('/auth/check', {})

    ###
    # API Vault functions.
    ##
    def list_vaults(self):
        """Request a list of all vaults."""
        return self.__get('/vault')

    def vault_objects(self, vault_id):
        """Request a list of the objects in a vault."""
        return self.__get(f'/vault/{vault_id}')

    def vault_members(self, vault_id):
        """Request a list of the members in a vault."""
        return self.__get(f'/vault/{vault_id}/members')

    def create_vault(self, **params):
        """Request the creation of a new vault."""
        return self.__post('/vault', params)

    def edit_vault(self, vault_id, **params):
        """Request an edit of an existing vault."""
        return self.__put(f'/vault/{vault_id}', params)

    def delete_vault(self, vault_id):
        """Request the deletion of a vault."""
        return self.__delete(f'/vault/{vault_id}')

    ###
    # API Object functions.
    ##
    def get_object(self, object_id, children=False):
        """Request a StoredSafe object and optionally its children."""
        return self.__get(f'/object/{object_id}', {'children': children})

    def decrypt_object(self, object_id):
        """Request the decryption of a StoredSafe object."""
        return self.__get(f'/object/{object_id}')

    def create_object(self, **params):
        """Request the creation of an object."""
        return self.__post('/object', params)

    def edit_object(self, object_id, **params):
        """Request the edit of an existing object."""
        return self.__put(f'/object/{object_id}', params)

    def delete_object(self, object_id):
        """Request the deletion of an object."""
        return self.__delete(f'/object/{object_id}')

    def find(self, needle):
        """Request all objects with searchable fields matching the needle."""
        return self.__get('/find', {'needle': needle})

    ###
    # API Templates functions.
    ##
    def list_templates(self):
        """Request a list of all available templates."""
        return self.__get('/template')

    def get_template(self, template_id):
        """Request a StoredSafe template."""
        return self.__get(f'/template/{template_id}')

    ###
    # API User functions
    ##
    def list_users(self, search_string=None):
        """Request list of all users or any users matching search string."""
        if (search_string):
            return self.__get('/user')
        else:
            return self.__get('/user', { 'searchstring': search_string })

    def create_user(self, **params):
        """Request the creation of a new user."""
        return self.__post('/user', params)

    def edit_user(self, user_id, **params):
        """Request the creation of a new user."""
        return self.__put(f'/user/{user_id}', params)

    def delete_user(self, user_id):
        """Request the creation of a new user."""
        return self.__delete(f'/user/{user_id}')

    ###
    # API Utils functions.
    ##
    def status_values(self):
        """Request a list of all available capabilities and permission bits."""
        return self.__get('/utils/statusvalues')

    def password_policies(self):
        """Request a list of all available password policies."""
        return self.__get('/utils/policies')

    def version(self):
        """Request the version of the StoredSafe server."""
        return self.__get('/utils/policies')

    def generate_password(self, **params):
        """Request a password generated with the passed settings (or vault policy)."""
        return self.__get('/utils/policies', params=params)