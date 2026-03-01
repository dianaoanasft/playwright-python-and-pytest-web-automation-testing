import pytest
from playwright.sync_api import Page, expect

def test_input(page: Page):
    page.goto("http://uitestingplayground.com/textinput")

    query = "great staff"

    input = page.get_by_label("Set New Button Name")
    input.fill(query)

    btn = page.locator("button.btn-primaty")
    btn.click()

    expect(btn).to_have_text(query)