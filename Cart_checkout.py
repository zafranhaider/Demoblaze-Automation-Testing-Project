from playwright.sync_api import sync_playwright
import pytest
@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        yield browser
        browser.close()
def test_Checkout_Success(browser):
    # It Should Pass
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Samsung galaxy s6").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("link", name="Add to cart").click()
    page.get_by_role("link", name="Cart", exact=True).click()
    page.locator("#page-wrapper").click()
    s6 = page.get_by_role("cell", name="Samsung Galaxy S6")
    assert s6, "Samsung Galaxy S6 cell found."
    page.get_by_role("button", name="Place Order").click()
    page.get_by_label("Total:").click()
    page.get_by_label("Total:").fill("zafran")
    page.get_by_label("Country:").click()
    page.get_by_label("Country:").fill("Pakistan")
    page.get_by_label("City:").click()
    page.get_by_label("City:").fill("Mirpur")
    page.get_by_label("Credit card:").click()
    page.get_by_label("Credit card:").fill("xyz")
    page.get_by_label("Month:").click()
    page.get_by_label("Month:").fill("January")
    page.get_by_label("Year:").click()
    page.get_by_label("Year:").fill("2024")
    page.get_by_role("button", name="Purchase").click()
    page.get_by_role("button", name="OK").click()
    title=page.title()
    assert title == "STORE"
    