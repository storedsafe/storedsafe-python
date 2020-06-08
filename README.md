# StoredSafe Python

Transparent Python wrapper for the StoredSafe REST-like API.

Full documentation of the API response signatures and more advanced paramters can be found at the [StoredSafe API Documentation](https://developer.storedsafe.com/).

For create and edit functions, parameters can be easily passed as keyword arguments, for example:
```python
api.create_vault(vaultname="My Vault", policy=7, description="Sercret")
```

Or if you're receiving data in dict-format, it can be unpacked into the function:
```python
data = function_that_returns_data()
api.create_vault(**data)
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
api.list_users(user_id) # List specific user
api.list_users(search_string) # Search for any user matching search_string
api.create_user(**params)
api.edit_user(user_id, **params)
api.delete_user(user_id)

# Utils
api.status_values()
api.password_policies()
api.version()
api.generate_password() # Use vault policy
api.generate_password(**params)
```
