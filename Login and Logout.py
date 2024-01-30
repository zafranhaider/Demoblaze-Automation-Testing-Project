# test_pytest.py
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
    page.goto("https://cms.must.edu.pk:8082/login.aspx")
    page.locator("#ddl_Session").select_option("FA21")
    page.locator("#ddl_Program").select_option("BIT")
    page.locator("#txt_RollNo").click()
    page.locator("#txt_RollNo").fill("064")
    page.locator("#txt_Password").click()
    
    page.locator("#txt_Password").fill(password)
    page.locator("#txt_Password").click()
    page.get_by_role("button", name="Sign In").click()
    title = page.title()
    assert title == 'Student Console'
def test_LoginFail_wrong_pasword(browser):
    page = browser.new_page()
    page.goto("https://cms.must.edu.pk:8082/login.aspx")
    page.locator("#ddl_Session").select_option("FA21")
    page.locator("#ddl_Program").select_option("BIT")
    page.locator("#txt_RollNo").click()
    page.locator("#txt_RollNo").fill("064")
    page.locator("#txt_Password").click()
    page.locator("#txt_Password").fill("123")
    page.locator("#txt_Password").click()
    page.get_by_role("button", name="Sign In").click()
    title = page.title()
    assert title == 'Student Console'
def test_LoginFail_wrong_Roll_NO(browser):
    page = browser.new_page()
    page.goto("https://cms.must.edu.pk:8082/login.aspx")
    page.locator("#ddl_Session").select_option("FA21")
    page.locator("#ddl_Program").select_option("BIT")
    page.locator("#txt_RollNo").click()
    page.locator("#txt_RollNo").fill("063")
    page.locator("#txt_Password").click()
    page.locator("#txt_Password").fill(password)
    page.locator("#txt_Password").click()
    page.get_by_role("button", name="Sign In").click()
    title = page.title()
    assert title == 'Student Console'
def test_LoginFail_wrong_Session(browser):
    page = browser.new_page()
    page.goto("https://cms.must.edu.pk:8082/login.aspx")
    page.locator("#ddl_Session").select_option("FA20")
    page.locator("#ddl_Program").select_option("BIT")
    page.locator("#txt_RollNo").click()
    page.locator("#txt_RollNo").fill("064")
    page.locator("#txt_Password").click()
    page.locator("#txt_Password").fill(password)
    page.locator("#txt_Password").click()
    page.get_by_role("button", name="Sign In").click()
    title = page.title()
    assert title == 'Student Console'
def test_LoginFail_wrong_Fild(browser):
    page = browser.new_page()
    page.goto("https://cms.must.edu.pk:8082/login.aspx")
    page.locator("#ddl_Session").select_option("FA21")
    page.locator("#ddl_Program").select_option("BIS")
    page.locator("#txt_RollNo").click()
    page.locator("#txt_RollNo").fill("064")
    page.locator("#txt_Password").click()
    page.locator("#txt_Password").fill(password)
    page.locator("#txt_Password").click()
    page.get_by_role("button", name="Sign In").click()
    title = page.title()
    assert title == 'Student Console'
def test_Student_Logout(browser):
    page = browser.new_page()
    page.goto("https://cms.must.edu.pk:8082/login.aspx")
    page.locator("#ddl_Session").select_option("FA21")
    page.locator("#ddl_Program").select_option("BIT")
    page.locator("#txt_RollNo").click()
    page.locator("#txt_RollNo").fill("064")
    page.locator("#txt_Password").click()
    page.locator("#txt_Password").fill(password)
    page.locator("#txt_Password").click()
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("link", name="Sign Out").click()
    title=page.title()
    assert title=="CMS :: Student Login"
def test_Student_Logout_failed(browser):
    page = browser.new_page()
    page.goto("https://cms.must.edu.pk:8082/login.aspx")
    page.locator("#ddl_Session").select_option("FA21")
    page.locator("#ddl_Program").select_option("BIT")
    page.locator("#txt_RollNo").click()
    page.locator("#txt_RollNo").fill("064")
    page.locator("#txt_Password").click()
    page.locator("#txt_Password").fill(password)
    page.locator("#txt_Password").click()
    page.get_by_role("button", name="Sign In").click()
    title=page.title()
    assert title=="CMS :: Student Login"



    
