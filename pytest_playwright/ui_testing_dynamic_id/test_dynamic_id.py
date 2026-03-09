import pytest
from playwright.sync_api import Page, expect

def test(page: Page):
    page.goto("http://uitestingplayground.com/dynamicid")

    button = page.get_by_role("button", name = "Button with Dynamic ID")
    expect(button).to_be_visible()

    button.click()