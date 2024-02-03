import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def login_page(browser):
    page = browser.new_page()
    return LoginPage(page)

def test_Login_Correct_Data(browser, login_page):
    login_page.goto_login_page()
    login_page.login_with_credentials('dab123', '123456')
    title = login_page.page.title()
    assert title == "STORE"

def test_Login_InCorrect_Data(browser, login_page):
    login_page.goto_login_page()
    login_page.login_with_credentials('dab1243', '1234567')
    error_message = login_page.get_error_message()
    assert "All Data Is Incorrect." in error_message

def test_Login_wrong_password(browser, login_page):
    login_page.goto_login_page()
    login_page.login_with_credentials('dab123', '1234567')
    error_message = login_page.get_error_message()
    assert "password is incorrect." in error_message

def test_Login_wrong_username(browser, login_page):
    login_page.goto_login_page()
    login_page.login_with_credentials('dab123456', '123456')
    error_message = login_page.get_error_message()
    assert "user does not exist." in error_message