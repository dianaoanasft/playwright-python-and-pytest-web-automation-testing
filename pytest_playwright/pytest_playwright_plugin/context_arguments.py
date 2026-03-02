import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500,
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "storage_state": "playwright/.auth/storage_state.json",
    }


def test_page_has_docs_link( page: Page)-> None:
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="Docs")

    expect(link).to_be_visible()

def test_visits_google_account(page: Page)-> None:
    page.goto("https://accounts.google.com")
    page.screenshot(path="account.jpg")