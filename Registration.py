# test_pytest
import pytest
from playwright.sync_api import sync_playwright
import os
@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()
password = os.environ.get('c_pas')
def test_LoginPass_correctdata(browser):
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
   