from playwright.sync_api import sync_playwright
import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
#It is a Cross Browser For These Scripts LOGIN,Add to cart,Checkout and Contact Us
#Almost 30 tests will be Done In One Go So Keep It in Headless Mod
#15 Should Be Passed And 15 Should Be failed Otherwise It's a Bug
# Define fixture to launch different browsers
@pytest.fixture(scope='function', params=['chromium', 'firefox', 'webkit'])
def browser(request):
    with sync_playwright() as p:
        browser = getattr(p, request.param).launch(headless=True)
        yield browser
        browser.close()

# Define login_page fixture
@pytest.fixture(scope='function')
def login_page(browser):
    page = browser.new_page()
    return LoginPage(page)

# Define cart_page fixture
@pytest.fixture(scope='function')
def cart_page(browser):
    page = browser.new_page()
    return CartPage(page)

# Define product_page fixture
@pytest.fixture(scope='function')
def product_page(browser):
    page = browser.new_page()
    return ProductPage(page)

# Test Login with Correct Data
def test_Login_Correct_Data(browser, login_page):
    login_page.goto_login_page()
    login_page.login_with_credentials('dab123', '123456')
    title = login_page.page.title()
    assert title == "STORE"

# Test Login with Incorrect Data
def test_Login_InCorrect_Data(browser, login_page):
    login_page.goto_login_page()
    login_page.login_with_credentials('dab1243', '1234567')
    error_message = login_page.get_error_message()
    assert "All Data Is Incorrect." in error_message

# Test Login with Wrong Password
def test_Login_wrong_password(browser, login_page):
    login_page.goto_login_page()
    login_page.login_with_credentials('dab123', '1234567')
    error_message = login_page.get_error_message()
    assert "password is incorrect." in error_message

# Test Login with Wrong Username
def test_Login_wrong_username(browser, login_page):
    login_page.goto_login_page()
    login_page.login_with_credentials('dab123456', '123456')
    error_message = login_page.get_error_message()
    assert "user does not exist." in error_message

# Test Adding to Cart
def test_adding_to_cart(browser, product_page):
    page = product_page.page
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Samsung galaxy s6").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    product_page.add_to_cart()
    cart_link = page.get_by_role("link", name="Cart", exact=True)
    cart_link.click()
    page.wait_for_timeout(3000)
    assert cart_link.is_visible(), "Cart link is visible"

# Test Item Quantity
def test_item_quantity(browser, product_page):
    page = product_page.page
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Samsung galaxy s6").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    product_page.add_to_cart()
    product_page.add_to_cart()
    cart_link = page.get_by_role("link", name="Cart", exact=True)
    cart_link.click()
    page.wait_for_timeout(3000)
    s6 = page.get_by_role("cell", name="Samsung Galaxy S6").first
    assert s6.is_visible(), "Samsung Galaxy S6 is visible"
    s6_second = page.get_by_role("cell", name="Samsung galaxy s6").nth(1)
    assert s6_second.is_visible(), "Samsung Galaxy S6 2nd is visible"

# Test Item Delete Should Not Be Visible
def test_item_delete_should_not_visible(browser):
    # It Should Pass because we successfully deleted the S6
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
    assert not s6.is_visible(), "Samsung Galaxy S6 cell is not visible it is Deleted"

# Test Item Checking After Delete Is Visible
def test_item_checking_after_delete_is_visible(browser):
    # It Should Fail because S6 should not be visible after Deleting
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
    assert s6.is_visible(), "Samsung Galaxy S6 cell is visible"

# Test Checkout Success
def test_Checkout_Success(browser):
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
    title = page.title()
    assert title == "STORE"

# Test SendData Success
def test_SendData_success(browser):
    # It Should Pass
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
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
    assert title == "STORE"
