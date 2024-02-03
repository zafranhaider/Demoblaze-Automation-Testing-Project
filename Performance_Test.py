import time
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright
from pages.product_page import ProductPage
#Please keep In Mind It is Just A BAsic Perofromance Test For a Good PErformance Test We 
#Should Always Use Proper Performance TOOL Like Jmeter or LoadRunner
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

def measure_login_time(login_page):
    start_time = time.time()
    login_page.goto_login_page()
    login_page.login_with_credentials('dab123', '123456')
    title = login_page.page.title()
    end_time = time.time()
    return end_time - start_time

def test_login_performance(browser, login_page):
    login_time = measure_login_time(login_page)
    assert login_time < 5, "Login process took more than 5 seconds."

@pytest.fixture(scope='function')
def product_page(browser):
    page = browser.new_page()
    return ProductPage(page)

def measure_add_to_cart_time(page, product_page):
    start_time = time.time()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Samsung galaxy s6").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    product_page.add_to_cart()
    cart_link = page.get_by_role("link", name="Cart", exact=True)
    cart_link.click()
    page.wait_for_timeout(3000)  # Wait for the cart to load
    end_time = time.time()
    return end_time - start_time

def test_add_to_cart_performance(browser, product_page):
    add_to_cart_time = measure_add_to_cart_time(product_page.page, product_page)
    assert add_to_cart_time < 5, "Adding to cart took more than 5 seconds."
def measure_checkout_time(page):
    start_time = time.time()
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
    end_time = time.time()
    return end_time - start_time

def test_checkout_performance(browser):
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Samsung galaxy s6").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("link", name="Add to cart").click()
    page.get_by_role("link", name="Cart", exact=True).click()
    page.locator("#page-wrapper").click()
    s6 = page.get_by_role("cell", name="Samsung Galaxy S6")
    assert s6, "Samsung Galaxy S6 cell found."
    checkout_time = measure_checkout_time(page)
    assert checkout_time < 10, "Checkout process took more than 10 seconds."

def measure_send_message_time(page):
    start_time = time.time()
    page.get_by_role("link", name="Contact").click()
    page.locator("#recipient-email").click()
    page.locator("#recipient-email").fill("zraaeae@gmail.com")
    page.get_by_label("Contact Email:").click()
    page.get_by_label("Contact Email:").fill("Zafran")
    page.get_by_label("Message:").click()
    page.get_by_label("Message:").fill("It Is Demo Test")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Send message").click()
    title = page.title()
    end_time = time.time()
    return end_time - start_time

def test_send_message_performance(browser):
    page = browser.new_page()
    send_message_time = measure_send_message_time(page)
    assert send_message_time < 5, "Sending message took more than 5 seconds."

