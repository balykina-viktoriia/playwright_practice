from playwright.sync_api import Page, expect

class LoginPage:
    URL = "https://www.saucedemo.com/"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
    def __init__(self, page: Page):
        self.page = page
        #Locators
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_locked_user = page.locator("[data-test='error']")

    def navigate(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_on_inventory_page(self):
        expect(self.page).to_have_url(self.INVENTORY_URL)

    def locked_out_user_login(self):
        expect(self.error_locked_user).to_have_text("Epic sadface: Sorry, this user has been locked out.")
