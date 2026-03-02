import pytest
from playwright.sync_api import Page, BrowserContext, expect

DOCS_URL = "https://playwright.dev/python/docs/intro"

def test_page_has_docs_link(context: BrowserContext, page: Page):

    page = context.new_page()
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="Docs")
    expect(link).to_be_visible()

def test_page_get_started_visits_docs(page: Page):
    page.goto("https://playwright.dev/python")
    get_started_link = page.get_by_role("link", name="GET STARTED")
    get_started_link.click()
    expect(page).to_have_url("https://playwright.dev/python/docs/intro")
