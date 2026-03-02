from playwright.sync_api import Page, expect
from models.login_page import LoginPage

def test_successful_login(page: Page):
    username="test"
    password="pwd"

    login_page = LoginPage(page)
    login_page.login(username, password)

    expect(login_page.label).to_have_text(f"Welcome, {username}!")

def test_failed_login(page: Page):
    username="test"
    password="1234"

    login_page = LoginPage(page)
    login_page.login(username, password)

    expect(login_page.label).to_have_text("Invalid username/password")