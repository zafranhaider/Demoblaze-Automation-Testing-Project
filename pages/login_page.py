class LoginPage:
    def __init__(self, page):
        self.page = page

    def goto_login_page(self):
        self.page.goto("https://www.demoblaze.com/")
        self.page.get_by_role("link", name="Log in").click()

    def login_with_credentials(self, username, password):
        self.page.locator("#loginusername").fill(username)
        self.page.locator("#loginpassword").fill(password)
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.page.get_by_role("button", name="Log in").click()

    def get_error_message(self):
        return self.page.inner_text('.alert-danger')
