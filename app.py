from creds import *
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled"])
        context = browser.new_context(storage_state="playwright/.auth/storage_state.json")
        

        page = context.new_page()
        page.goto("https://accounts.google.com")

        #email = page.get_by_label("Email or phone")
        #email.fill(EMAIL)
        #page.get_by_role("button", name="Next").click()

        #password = page.get_by_label("Enter your password")
        #password.fill(PASSWORD)
        #page.get_by_role("button", name="Next").click()
        
        page.pause()

        context.close()
