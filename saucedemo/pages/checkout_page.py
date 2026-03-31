from playwright.sync_api import Page, expect

class CheckoutPage:
    URL = "https://www.saucedemo.com/checkout-step-one.html"
    CHECKOUT_URL = "https://www.saucedemo.com/checkout-step-two.html"
    COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.zip_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.complete_page = page.locator("[data-test='complete-header']")
        self.error_problem_user = page.locator("[data-test='error']")

    def expect_on_checkout_page(self):
        expect(self.page).to_have_url(self.URL)

    def get_your_information(self, first_name, last_name, zip_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.zip_code_input.fill(zip_code)
        self.continue_button.click()

    def checkout_overview(self):
        expect(self.page).to_have_url(self.CHECKOUT_URL)
        self.finish_button.click()

    def checkout_success(self):
        expect(self.page).to_have_url(self.COMPLETE_URL)
        expect(self.complete_page).to_have_text("Thank you for your order!")

    def problem_user_checkout(self, first_name, last_name, zip_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.zip_code_input.fill(zip_code)
        self.continue_button.click()
        expect(self.error_problem_user).to_have_text("Error: Last Name is required")


