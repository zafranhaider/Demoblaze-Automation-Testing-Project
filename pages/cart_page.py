# cart_page.py
class CartPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_cart(self):
        self.page.get_by_role("link", name="Cart", exact=True).click()

    def delete_item(self):
        self.page.locator("#page-wrapper").click()
        self.page.get_by_role("link", name="Delete").click()

    def is_item_visible(self, item_name):
        return self.page.get_by_role("cell", name=item_name).is_visible()