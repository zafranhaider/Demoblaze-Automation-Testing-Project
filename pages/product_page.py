class ProductPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self):
        self.page.get_by_role("link", name="Add to cart").click()