import pytest
from playwright.sync_api import sync_playwright
from pages.cart_page import CartPage
from pages.product_page import ProductPage

@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def cart_page(browser):
    page = browser.new_page()
    return CartPage(page)

@pytest.fixture(scope='function')
def product_page(browser):
    page = browser.new_page()
    return ProductPage(page)

def test_adding_to_cart(browser, product_page):
    page = product_page.page
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Samsung galaxy s6").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    product_page.add_to_cart()
    cart_link = page.get_by_role("link", name="Cart", exact=True)
    cart_link.click()
    page.wait_for_timeout(3000)  # Corrected wait_for_timeout call
    assert cart_link.is_visible(), "Cart link is visible"

def test_item_quantity(browser, product_page):
    page = product_page.page
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Samsung galaxy s6").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    product_page.add_to_cart()
    product_page.add_to_cart()
    cart_link = page.get_by_role("link", name="Cart", exact=True)
    cart_link.click()
    page.wait_for_timeout(3000)  # Corrected wait_for_timeout call
    s6 = page.get_by_role("cell", name="Samsung Galaxy S6").first
    assert s6.is_visible(), "Samsung Galaxy S6 is visible"
    s6_second = page.get_by_role("cell", name="Samsung galaxy s6").nth(1)
    assert s6_second.is_visible(), "Samsung Galaxy S6 2nd is visible"
    
def test_item_delete_should_not_visible(browser):
    # It Should Pass becuase we successfully deleted the S6
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Samsung galaxy s6").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("link", name="Add to cart").click()
    page.get_by_role("link", name="Cart", exact=True).click()
    page.locator("#page-wrapper").click()
    page.get_by_role("link", name="Delete").click()
    s6 = page.get_by_role("cell", name="Samsung Galaxy S6")
    page.wait_for_timeout(3000)
    assert not s6.is_visible(), "Samsung Galaxy S6 cell is not vissible it is Deleted"
def test_item_checking_after_delete_is_visible(browser):
    # It Should Fail Becuase S6 should not be visible after Deleting
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Samsung galaxy s6").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("link", name="Add to cart").click()
    page.get_by_role("link", name="Cart", exact=True).click()
    page.locator("#page-wrapper").click()
    page.get_by_role("link", name="Delete").click()
    s6 = page.get_by_role("cell", name="Samsung Galaxy S6")
    page.wait_for_timeout(3000)
    assert s6.is_visible(), "Samsung Galaxy S6 cell is visible" #It should Fail 