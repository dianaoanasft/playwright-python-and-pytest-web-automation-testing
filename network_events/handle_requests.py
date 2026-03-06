from playwright.sync_api import Route, Page, expect

def on_route(route: Route):
    print("Request aborted:", route.request)
    route.abort()

def test_docs_link(page: Page):
    page.route(
        "**/*.png",
        on_route
    )

    page.goto("https://playwright.dev/python")

    page.screenshot(path="playwright.jpg", full_page=True)