from playwright.sync_api import sync_playwright
import pytest
@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        yield browser
        browser.close()
def test_adding_to_cart(browser):
    # It Should Pass
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Samsung galaxy s6").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("link", name="Add to cart").click()
    page.get_by_role("link", name="Cart", exact=True).click()
    page.locator("#page-wrapper").click()
    s6 = page.get_by_role("cell", name="Samsung Galaxy S6")
    assert s6, "Samsung Galaxy S6 cell found."
def test_item_quantity(browser):
    # It Should pass duo to correct quantity
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Samsung galaxy s6").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("link", name="Add to cart").click()
    page.get_by_role("link", name="Add to cart").click()
    page.get_by_role("link", name="Cart", exact=True).click()
    page.locator("#page-wrapper").click()
    s6 = page.get_by_role("cell", name="Samsung Galaxy S6").first
    page.wait_for_timeout(3000)
    assert s6.is_visible(), "Samsung Galaxy S6 " 
    s6= page.get_by_role("cell", name="Samsung galaxy s6").nth(1)
    page.wait_for_timeout(3000)
    assert s6.is_visible(), "Samsung Galaxy S6 2nd is visible " 
    
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
