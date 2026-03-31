from playwright.sync_api import Page, expect

class CartPage:
    CART_URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        self.page = page
        self.cart_item = page.locator("[data-test='inventory-item-name']")
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def expect_on_cart_page(self):
        expect(self.page).to_have_url(self.CART_URL)

    def check_cart_item(self):
        expect(self.cart_item).to_be_visible()

    def go_to_checkout(self):
        self.checkout_button.click()