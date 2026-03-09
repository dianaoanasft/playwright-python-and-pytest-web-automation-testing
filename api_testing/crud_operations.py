import json
import pytest
from playwright.sync_api import *

@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = api_context = playwright.request.new_context(
        base_url="https://dummyjson.com",
        extra_http_headers={ 'Content-Type': 'application/json' },
    )

    yield api_context
    api_context.dispose()

def test_create_user(api_context: APIRequestContext):
    response = api_context.post(
        "users/add",
        data={
            "firstName": "Diana",
            "lastName": "Test",
            "age": 28
        }
    )
    user_data = response.json()
    assert user_data["id"] == 209
    assert user_data["firstName"] == "Diana"

def test_update_user(api_context: APIRequestContext):
   print(api_context.get("users/2").json()["lastName"])

   response = api_context.put(
       "users/2",
       data={
           "lastName": "Test",
           "age": 20,
       }
   )
   user_data = response.json()

   print(user_data)
   assert user_data["lastName"] == "Test"
   assert user_data["age"] == 20
    