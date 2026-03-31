from playwright.sync_api import Page
from saucedemo.pages.login_page import LoginPage
from saucedemo.pages.inventory_page import InventoryPage
from saucedemo.pages.cart_page import CartPage
from saucedemo.pages.checkout_page import CheckoutPage


def test_checkout_flow(page: Page):
    page.set_default_timeout(10000)

    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    login_page.expect_on_inventory_page()

    inventory_page = InventoryPage(page)

    inventory_page.add_to_cart()
    inventory_page.expect_remove_button()
    inventory_page.check_shopping_cart_bage()
    inventory_page.go_to_cart()

    cart_page = CartPage(page)

    cart_page.expect_on_cart_page()
    cart_page.check_cart_item()
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(page)

    checkout_page.expect_on_checkout_page()
    checkout_page.get_your_information("Viktoriia", "Balykina", "1111")
    checkout_page.checkout_overview()
    checkout_page.checkout_success()

def test_locked_out_user_flow(page: Page):
    page.set_default_timeout(10000)

    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")
    login_page.locked_out_user_login()

def test_problem_user_flow(page: Page):
    page.set_default_timeout(10000)

    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("problem_user", "secret_sauce")
    login_page.expect_on_inventory_page()

    inventory_page = InventoryPage(page)

    inventory_page.add_to_cart()
    inventory_page.expect_remove_button()
    inventory_page.check_shopping_cart_bage()
    inventory_page.go_to_cart()

    cart_page = CartPage(page)

    cart_page.expect_on_cart_page()
    cart_page.check_cart_item()
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(page)

    checkout_page.expect_on_checkout_page()
    checkout_page.problem_user_checkout("Viktoriia", "Balykina", "1111")
