import pytest
from playwright.sync_api import Page, expect

def test_scrollbars(page: Page):
    page.goto("http://uitestingplayground.com/scrollbars")

    btn = page.get_by_role("button", name="Hiding Button")
    btn.click()
    btn.screenshot(path="test-scrollbars.jpg")