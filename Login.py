from playwright.sync_api import sync_playwright
import pytest
@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        yield browser
        browser.close()
def test_Login_Correct_Data(browser):
    # It Should Pass
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Log in").click()
    page.locator("#loginusername").fill('dab123')
    page.locator("#loginpassword").fill('123456')
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Log in").click()
    title=page.title()
    assert title =="STORE"
def test_Login_InCorrect_Data(browser):
    # It Should Fail
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Log in").click()
    page.locator("#loginusername").fill('dab1243')
    page.locator("#loginpassword").fill('1234567')
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Log in").click()
    error_message = page.inner_text('.alert-danger')
    assert "All Data Is Incorrect." in error_message
def test_Login_wrong_password(browser):
    # It Should Fail
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Log in").click()
    page.locator("#loginusername").fill('dab123')
    page.locator("#loginpassword").fill('1234567')
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Log in").click()
    error_message = page.inner_text('.alert-danger')
    assert "password is incorrect." in error_message
def test_Login_wrong_username(browser):
    # It Should Fail
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Log in").click()
    page.locator("#loginusername").fill('dab123456')
    page.locator("#loginpassword").fill('123456')
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Log in").click()
    error_message = page.inner_text('.alert-danger')
    assert "user does not exist." in error_message
   

