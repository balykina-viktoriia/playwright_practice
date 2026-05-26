from playwright.sync_api import Page, expect
from saucedemo.test_data import Users, CustomerData, ErrorMessages, InventoryItems
from saucedemo.pages.login_page import LoginPage


def test_checkout_flow(logged_in_page, cart_page, checkout_page):
    inventory_page = logged_in_page

    inventory_page.add_to_cart(InventoryItems.BACKPACK)
    inventory_page.check_shopping_cart_badge(1)
    inventory_page.go_to_cart()

    cart_page.expect_on_cart_page()
    cart_page.check_cart_item()
    cart_page.go_to_checkout()

    checkout_page.expect_on_checkout_page()
    checkout_page.get_your_information(**CustomerData.VALID)
    checkout_page.expect_on_step_two_page()
    checkout_page.finish_checkout()
    checkout_page.checkout_success()


def test_problem_user_flow(login_as, cart_page, checkout_page):
    inventory_page = login_as(Users.PROBLEM)

    inventory_page.add_to_cart(InventoryItems.BACKPACK)
    inventory_page.check_shopping_cart_badge(1)
    inventory_page.go_to_cart()

    cart_page.expect_on_cart_page()
    cart_page.check_cart_item()
    cart_page.go_to_checkout()

    checkout_page.expect_on_checkout_page()
    checkout_page.get_your_information(**CustomerData.VALID)
    expect(checkout_page.error_message).to_have_text(ErrorMessages.LAST_NAME_REQUIRED)


def test_locked_out_user_flow(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(**Users.LOCKED_OUT)
    expect(login_page.error_message).to_have_text(ErrorMessages.LOCKED_OUT)
