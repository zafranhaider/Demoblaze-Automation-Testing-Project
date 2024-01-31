# test_pytest.py
import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
def Registration(browser):
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    title=page.title()
    assert title =="STORE"



   