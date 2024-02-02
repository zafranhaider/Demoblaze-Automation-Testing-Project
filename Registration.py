# test_pytest.py
import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
def test_Registration(browser): 
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("dab123")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("123456")
    page.get_by_label("Password:").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Sign up").click()
    title=page.title()
    assert title == "STORE"
def test_Registration_Same_data(browser): 
    #It should Fail
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("dab123")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("123456")
    page.get_by_label("Password:").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Sign up").click()
    error_message=page.inner_text('.alert.danger')
    assert "Same Registration data" in error_message

    





   