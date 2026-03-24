import re

from playwright.sync_api import Page, expect


def test_checkout_flow(page: Page):
    page.set_default_timeout(10000)

    # Login
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_url("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # Add item to cart
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.get_by_role("button", name="Add to cart").first.click()
    expect(page.get_by_role("button", name="Remove")).to_be_visible()
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")

    # Go to cart
    page.locator("[data-test='shopping-cart-link']").click()
    expect(page.locator("[data-test='inventory-item-name']")).to_be_visible()

    # Checkout - step 1
    page.get_by_role("button", name="Checkout").click()
    page.get_by_placeholder("First Name").fill("Viktoria")
    page.get_by_placeholder("Last Name").fill("Balykina")
    page.get_by_placeholder("Zip/Postal Code").fill("1111")
    page.get_by_role("button", name="Continue").click()

    # Checkout - step 2
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    page.get_by_role("button", name="Finish").click()
    expect(page.locator("[data-test='complete-header']")).to_have_text("Thank you for your order!")