from playwright.sync_api import Page, expect

class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page
    @property
    def add_to_cart_buttons(self):
        return self.page.locator("[data-test*='add-to-cart']")

    @property
    def remove_buttons(self):
        return self.page.locator("[data-test*='remove']")

    @property
    def cart_badge(self):
        return self.page.locator("[data-test='shopping-cart-badge']")

    @property
    def cart_link(self):
        return self.page.locator("[data-test='shopping-cart-link']")

    def add_to_cart(self, index):
        self.add_to_cart_buttons.nth(index).click()

    def expect_remove_button(self):
        expect(self.remove_buttons).to_be_visible()

    def remove_from_cart(self, index):
        self.remove_buttons.nth(index).click()

    def check_shopping_cart_badge(self, items_number):
        expect(self.cart_badge).to_have_text(str(items_number))

    def empty_shopping_cart_badge(self):
        expect(self.page.locator("[data-test='shopping-cart-badge']")).not_to_be_visible()

    def go_to_cart(self):
        self.cart_link.click()
