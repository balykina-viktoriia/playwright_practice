from playwright.sync_api import Page, expect

class LoginPage:
    URL = "https://www.saucedemo.com/"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
    ERROR_LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."
    def __init__(self, page: Page):
        self.page = page
        #Locators

    @property
    def username_input(self):
        return self.page.get_by_placeholder("Username")

    @property
    def password_input(self):
        return self.page.get_by_placeholder("Password")

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Login")

    @property
    def error_message(self):
        return self.page.locator("[data-test='error']")

    def navigate(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_on_inventory_page(self):
        expect(self.page).to_have_url(self.INVENTORY_URL)

