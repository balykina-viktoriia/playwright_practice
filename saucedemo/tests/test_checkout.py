import pytest
from playwright.sync_api import Page, expect
from saucedemo.test_data import Users
from saucedemo.pages.login_page import LoginPage
from saucedemo.pages.inventory_page import InventoryPage
from saucedemo.pages.cart_page import CartPage
from saucedemo.pages.checkout_page import CheckoutPage

@pytest.mark.parametrize("user, checkout_method", [
    (Users.STANDARD, "get_your_information"),
    (Users.PROBLEM, "problem_user_checkout"),
])
def test_checkout_flow(page: Page, user, checkout_method):

    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(**user)
    login_page.expect_on_inventory_page()

    inventory_page = InventoryPage(page)

    inventory_page.add_to_cart()
    inventory_page.expect_remove_button()
    inventory_page.check_shopping_cart_badge()
    inventory_page.go_to_cart()

    cart_page = CartPage(page)

    cart_page.expect_on_cart_page()
    cart_page.check_cart_item()
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(page)

    checkout_page.expect_on_checkout_page()
    getattr(checkout_page, checkout_method)("Viktoriia", "Balykina", "1111")
    if checkout_method == "get_your_information":
        checkout_page.checkout_overview()
        checkout_page.checkout_success()

def test_locked_out_user_flow(page: Page):

    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(**Users.LOCKED_OUT)
    expect(login_page.error_message).to_have_text(LoginPage.ERROR_LOCKED_OUT)
