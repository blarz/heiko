
# Heiko

Heiko is a frontend for [MaaS](https://github.com/k4cg/matomat-service)
and a MVP client to be run in K4CG

# Install

```
pip install -r requirements
```

# Run

```
./heiko
```


# Development:

## swagger-client
MaaS (Matomat as a Service) API definition

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.5.2
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/k4cg/heiko.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/k4cg/heiko.git`)

Then import the package:
```python
import swagger_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.AuthApi()
username = 'username_example' # str |
password = 'password_example' # str |
validityseconds = 56 # int |  (optional)

try:
    # Logs a user in and returns an JWT token for authentication
    api_response = api_instance.auth_login_post(username, password, validityseconds=validityseconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_login_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost:8443/v0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**auth_login_post**](docs/AuthApi.md#auth_login_post) | **POST** /auth/login | Logs a user in and returns an JWT token for authentication
*ItemsApi* | [**items_get**](docs/ItemsApi.md#items_get) | **GET** /items | List all available items
*ItemsApi* | [**items_item_id_consume_patch**](docs/ItemsApi.md#items_item_id_consume_patch) | **PATCH** /items/{itemId}/consume | Consumes a Item
*ItemsApi* | [**items_item_id_delete**](docs/ItemsApi.md#items_item_id_delete) | **DELETE** /items/{itemId} | Delete Item
*ItemsApi* | [**items_item_id_get**](docs/ItemsApi.md#items_item_id_get) | **GET** /items/{itemId} | Get a certain Item
*ItemsApi* | [**items_item_id_patch**](docs/ItemsApi.md#items_item_id_patch) | **PATCH** /items/{itemId} | Update Item
*ItemsApi* | [**items_item_id_stats_get**](docs/ItemsApi.md#items_item_id_stats_get) | **GET** /items/{itemId}/stats | Get consumption stats
*ItemsApi* | [**items_post**](docs/ItemsApi.md#items_post) | **POST** /items | Add a new item
*ItemsApi* | [**items_stats_get**](docs/ItemsApi.md#items_stats_get) | **GET** /items/stats | Get consumption stats of all items
*ServiceApi* | [**service_stats_get**](docs/ServiceApi.md#service_stats_get) | **GET** /service/stats | Total service stats
*UsersApi* | [**users_get**](docs/UsersApi.md#users_get) | **GET** /users | List all users
*UsersApi* | [**users_post**](docs/UsersApi.md#users_post) | **POST** /users | Add a new user
*UsersApi* | [**users_user_id_credits_add_patch**](docs/UsersApi.md#users_user_id_credits_add_patch) | **PATCH** /users/{userId}/credits/add | Add users credits
*UsersApi* | [**users_user_id_credits_transfer_patch**](docs/UsersApi.md#users_user_id_credits_transfer_patch) | **PATCH** /users/{userId}/credits/transfer | Transfer credits
*UsersApi* | [**users_user_id_credits_withdraw_patch**](docs/UsersApi.md#users_user_id_credits_withdraw_patch) | **PATCH** /users/{userId}/credits/withdraw | Widthdraw users credits
*UsersApi* | [**users_user_id_delete**](docs/UsersApi.md#users_user_id_delete) | **DELETE** /users/{userId} | Delete user
*UsersApi* | [**users_user_id_get**](docs/UsersApi.md#users_user_id_get) | **GET** /users/{userId} | Get user by user ID
*UsersApi* | [**users_user_id_password_patch**](docs/UsersApi.md#users_user_id_password_patch) | **PATCH** /users/{userId}/password | Change password for currently logged in user.
*UsersApi* | [**users_user_id_resetpassword_patch**](docs/UsersApi.md#users_user_id_resetpassword_patch) | **PATCH** /users/{userId}/resetpassword | Set password for user ID
*UsersApi* | [**users_user_id_stats_get**](docs/UsersApi.md#users_user_id_stats_get) | **GET** /users/{userId}/stats | Get matomat stats for user


## Documentation For Models

 - [AuthSuccess](docs/AuthSuccess.md)
 - [Error](docs/Error.md)
 - [Item](docs/Item.md)
 - [ItemStats](docs/ItemStats.md)
 - [ServiceStats](docs/ServiceStats.md)
 - [ServiceStatsItems](docs/ServiceStatsItems.md)
 - [ServiceStatsItemsCost](docs/ServiceStatsItemsCost.md)
 - [ServiceStatsUsers](docs/ServiceStatsUsers.md)
 - [ServiceStatsUsersCredits](docs/ServiceStatsUsersCredits.md)
 - [TransferredCredits](docs/TransferredCredits.md)
 - [User](docs/User.md)
 - [UserStats](docs/UserStats.md)


## Documentation For Authorization


## jwtTokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

@noqqe

