# test_pytest.py
import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()
def test_Registration_nomraldata(browser): 
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
def test_Registration_special_chracter(browser): 
    #It is a Bug no special character should be taken
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("dab@123")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("123456")
    page.get_by_label("Password:").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Sign up").click()
    title=page.title()
    assert title == "STORE"
def test_Registration_tooshort_user(browser): 
    #It is A Bug user is too short
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("da3")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("123456")
    page.get_by_label("Password:").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Sign up").click()
    title=page.title()
    assert title == "STORE"
def test_Registration_toolong_user(browser): 
    #It is A Bug User is too long
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("dab123wwwwwwwwwwwwwwwwwwwww")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("123456")
    page.get_by_label("Password:").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Sign up").click()
    title=page.title()
    assert title == "STORE"
def test_Registration_same_pasword_as_username(browser): 
    #It is A Bug Pasword is same as user
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("1234")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("1234")
    page.get_by_label("Password:").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Sign up").click()
    title=page.title()
    assert title == "STORE"
#There are alot of bug like This You can Increase the Test Cases By adding More

    





   