# StoredSafe Python

Transparent Python wrapper for the StoredSafe REST-like API.

Full documentation of the API response signatures and more advanced parameters can be found at the [StoredSafe API Documentation](https://developer.storedsafe.com/).


## Install

Install [storedsafe](https://pypi.org/project/storedsafe/) from pypi.
```bash
pip install storedsafe
```

## Examples

### Login

```python
# Initial configuration
api = StoredSafe(host='my.site.com', apikey='my-apikey')

# Login using TOTP
api.login_totp(username='my-username', passphrase='my-passphrase', otp='my-timed-otp')

# Login using YubiKey
api.login_yubikey(username='my-username', passphrase='my-passphrase', otp='my-yubico-otp')

# Login using client certificate
# 3rd party software may be required to get the certificate data from your smartcard
api.login_smartcard(username='my-username', passphrase='my-passphrase', cert='/path/to/cert', key='/path/to/key')
```

In the event you already have a token, you can skip the previous step and input the token directly.
```python
api = StoredSafe(host='my.site.com', token='my-storedsafe-token')
```

If you're using the [StoredSafe tokenhandler](https://github.com/storedsafe/tokenhandler), you can also retrieve the host, apikey and token from an rc-file:
```python
# Default rc location
api = StoredSafe.from_rc()

# Custom rc location
api = StoredSafe.from_rc(path='/path/to/rc-file')
```

### Programming styles

For create and edit methods, parameters can be easily passed as keyword arguments, for example:
```python
api.create_vault(vaultname="My Vault", policy=7, description="Sercret")
```

Or if you're receiving data in dict-format, it can be unpacked into the method:
```python
data = function_that_returns_data()
api.create_vault(**data)
```

### Return types

The return value of all methods is a [`requests` response object](https://requests.readthedocs.io/en/latest/api/#requests.Response). To obtain the data returned by a successful response object, you can use the `json()` function:
```python
res = api.list_vaults()
if res.status_code <= 403:
    data = res.json()
    if res.ok:
        print(data['VAULTS'])
    else:
        print(data['ERRORS'])
```

### Files

Files are returned as a base64 string and must be decoded to restore the original state of the file.
```python
import base64

res = api.get_file(object_id)
data = res.json()
filedata = base64.urlsafe_b64decode(data['FILEDATA'])
filedata_utf8 = filedata.decode('utf-8') # If you want to use UTF-8 encoding
with open(path, 'w') as f:
    f.write(filedata_utf8)
```

## Usage

```python
from storedsafe import StoredSafe

# Manual configuration
api = StoredSafe(host='my.site.com', apikey='my-apikey', token='my-storedsafe-token')

# Automatic configuration
api = StoredSafe.from_rc() # Use default path ~/.storedsafe-client.rc
api = StoredSafe.from_rc(path='/path/to/rc-file')

# Auth
api.login_totp(username='my-username', passphrase='my-passphrase', otp='my-otp')
api.login_yubikey(username='my-username', passphrase='my-passphrase', otp='my-otp')
api.login_smartcard(username='my-username', passphrase='my-passphrase', cert='/path/to/cert', key='/path/to/key')
api.logout()
api.check()

# Vaults
api.list_vaults()
api.vault_objects(vault_id) # String or integer
api.vault_members(vault_id)
api.create_vault(**params) # See parameters in API documentation
api.edit_vault(vault_id, **params)
api.delete_vault(vault_id)

# Objects
api.get_object(object_id) # String or integer
api.get_object(object_id, children=True) # children False by default
api.decrypt_object(object_id)
api.get_file(object_id) # Decrypt file and get base64 version of file
api.get_mime_type(file_path) # Get mimetype and max file upload size
api.filecollect(file_path) # Get the suggested template for the file
api.upload_file(file_path, **params)
api.create_object(**params)
api.edit_object(object_id, **params)
api.delete_object(object_id)

# Users
api.list_users() # List all users
api.list_users(search_string) # Search for any user matching search_string
api.get_user(user_id)
api.create_user(**params)
api.edit_user(user_id, **params)
api.delete_user(user_id)

# Utils
api.status_values()
api.password_policies()
api.version()
api.generate_password() # Use default settings
api.generate_password(**params)
```

## Requests parameters

In version `1.2.0+`, parameters can be passed directly to the requests library through various methods.

Requests parameters can be applied directly to the StoredSafe API object:

```python
from storedsafe import StoredSafe

requests_options = {
    'timeout': 10,
    'verify': ca_path
}
api = StoredSafe(host='my.site.com', apikey='my-apikey', token='my-storedsafe-token', **requests_options)

# Adjust requests can be adjusted later through the `requests_options` attribute
api.requests_options['timeout'] = 5
```

Or when calling any of the API methods:

```python
api.create_user(**user_params, timeout=10)
```

Options passed to one of the API methods will take precedence over the options defined on the StoredSafe object.
