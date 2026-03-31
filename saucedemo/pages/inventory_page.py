from playwright.sync_api import Page, expect

class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart").first
        self.remove_button = page.get_by_role("button", name="Remove")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def expect_remove_button(self):
        expect(self.remove_button).to_be_visible()

    def check_shopping_cart_bage(self):
        expect(self.cart_badge).to_have_text("1")

    def go_to_cart(self):
        self.cart_link.click()
