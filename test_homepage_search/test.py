from playwright.sync_api import Page, expect
from models.home_page import HomePage

def test_docs_link(page: Page):
    homepage = HomePage(page)
    homepage.visit_docs()
    expect(homepage.page).to_have_url("https://playwright.dev/python/docs/intro")


def test_docs_search(page: Page):
    query = "assertions"
    homepage = HomePage(page)
    homepage.search(query)

    expect(homepage.search_results()).to_contain_text("List of assertions")