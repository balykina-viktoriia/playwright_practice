from playwright.sync_api import Page, expect

class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page
    @property
    def add_to_cart_button(self):
        return self.page.get_by_role("button", name="Add to cart").first

    @property
    def remove_button(self):
        return self.page.get_by_role("button", name="Remove")

    @property
    def cart_badge(self):
        return self.page.locator("[data-test='shopping-cart-badge']")

    @property
    def cart_link(self):
        return self.page.locator("[data-test='shopping-cart-link']")

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def expect_remove_button(self):
        expect(self.remove_button).to_be_visible()

    def check_shopping_cart_badge(self):
        expect(self.cart_badge).to_have_text("1")

    def go_to_cart(self):
        self.cart_link.click()
