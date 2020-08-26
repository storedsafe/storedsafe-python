# StoredSafe Python

Transparent Python wrapper for the StoredSafe REST-like API.

Full documentation of the API response signatures and more advanced paramters can be found at the [StoredSafe API Documentation](https://developer.storedsafe.com/).

## Examples
For create and edit methods, parameters can be easily passed as keyword arguments, for example:
```python
api.create_vault(vaultname="My Vault", policy=7, description="Sercret")
```

Or if you're receiving data in dict-format, it can be unpacked into the method:
```python
data = function_that_returns_data()
api.create_vault(**data)
```

The return value of all methods is a [`requests` response object](https://requests.readthedocs.io/en/latest/api/#requests.Response). To obtain the data returned by a successful response object, you can use the `json()` function:
```python
r = api.list_vaults()
if <= 403:
    data = res.json()
    if res.ok:
        print(data['VAULTS'])
    else:
        print(data['ERRORS'])
```

## Usage

```python
from storedsafe import StoredSafe
api = StoredSafe('my.site.com', 'my-api-key')

# Auth
api.login_totp('username', 'passphrase', 'otp')
api.login_yubikey('username', 'passphrase', 'otp')
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
