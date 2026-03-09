import pytest
from playwright.sync_api import Page, expect

def test(page: Page):
    page.goto("http://uitestingplayground.com/classattr")

    primary_btn = page.locator("button.btn-primary")

    #primary_btn = page.locator("//button[ contains(@class, 'btn-primary') ]")

    expect(primary_btn).to_be_visible()

    button.click()