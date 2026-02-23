import pytest
from playwright.sync_api import Page, expect

DOCS_URL = "https://playwright.dev/python/docs/intro"

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")


    #link = page.get_by_role("link", name="GET STARTED")
    #heading = page.locator("h1.hero__title")
    #docs_link = page.get_by_role("link", name="Docs")
    input = page.get_by_placeholder("Search docs")

    #assert page.url == DOCS_URL
    #expect(page).to_have_url(DOCS_URL)
    #expect(page).to_have_title("Installation | Playwright Python")
    #expect(link).to_be_visible()
    #expect(link).to_be_enabled()
    #expect(heading).to_contain_text("testing")
    #expect(docs_link).to_have_class("navbar__item navbar__link")

    #input is hidden before button click
    expect(input).to_be_hidden()
    #search button
    search_btn = page.get_by_role("button", name="Search")
    search_btn.press("Control+KeyK")
    
    # should pop the serch menu
    expect(input).to_be_editable()
    expect(input).to_be_empty()

    #type some query in the input
    query = "assertions"
    input.fill(query)

    #check input value
    expect(input).to_have_value(query)


