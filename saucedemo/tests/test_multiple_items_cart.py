import pytest
from playwright.sync_api import Page, expect
from saucedemo.test_data import Users
from saucedemo.pages.login_page import LoginPage
from saucedemo.pages.inventory_page import InventoryPage

@pytest.mark.parametrize("user", [
    (Users.STANDARD),
    (Users.PROBLEM),
])

def test_add_multiple_items (page: Page, user):

    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(**user)
    login_page.expect_on_inventory_page()

    inventory_page = InventoryPage(page)

    inventory_page.add_to_cart(1)
    inventory_page.add_to_cart(3)
    inventory_page.expect_remove_button()
    inventory_page.check_shopping_cart_badge(2)

@pytest.mark.parametrize("user", [
    (Users.STANDARD),
    (Users.PROBLEM),
])

def test_remove_multiple_items (page: Page, user):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(**user)
    login_page.expect_on_inventory_page()

    inventory_page = InventoryPage(page)

    inventory_page.add_to_cart(1)
    inventory_page.add_to_cart(3)
    inventory_page.expect_remove_button()
    inventory_page.check_shopping_cart_badge(2)

    inventory_page.remove_from_cart(1)
    inventory_page.remove_from_cart(3)
    inventory_page.empty_shopping_cart_badge()
