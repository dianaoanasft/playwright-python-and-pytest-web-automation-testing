import json
import pytest
from playwright.sync_api import *

@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
    )

    yield api_context
    api_context.dispose()

def test_users_api(api_context: APIRequestContext):

    response = api_context.get("/users/3")
    
    user_data = response.json()

    assert "firstName" in user_data
    assert "lastName" in user_data

    assert user_data["firstName"] == "Sophia"
    assert user_data["lastName"] == "Brown"