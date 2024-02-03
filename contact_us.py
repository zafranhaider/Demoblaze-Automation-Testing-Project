from playwright.sync_api import sync_playwright
import pytest
@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        yield browser
        browser.close()
def test_SendData_success(browser):
    # It Should Pass
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Contact").click()
    page.locator("#recipient-email").click()
    page.locator("#recipient-email").fill("zraaeae@gmail.com")
    page.get_by_label("Contact Email:").click()
    page.get_by_label("Contact Email:").fill("Zafran")
    page.get_by_label("Message:").click()
    page.get_by_label("Message:").fill("It Is Demo Test")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Send message").click()
    title=page.title()
    assert title == "STORE"
    page.pause()