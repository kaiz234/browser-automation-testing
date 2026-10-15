"""Example browser functional tests using pytest and Playwright."""

import os
import re

from playwright.sync_api import Page, expect

BASE_URL = os.getenv("DEMO_BASE_URL", "https://www.saucedemo.com/")
USERNAME = os.getenv("DEMO_USERNAME", "standard_user")
PASSWORD = os.getenv("DEMO_PASSWORD", "secret_sauce")


def login(page: Page, username: str, password: str) -> None:
    """Open the demo application and submit its login form."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.locator('[data-test="username"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[data-test="login-button"]').click()


def test_login_page_displays_expected_fields(page: Page) -> None:
    """The login page should show the username, password, and login controls."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    expect(page.locator('[data-test="username"]')).to_be_visible()
    expect(page.locator('[data-test="password"]')).to_be_visible()
    expect(page.locator('[data-test="login-button"]')).to_be_visible()


def test_valid_login_opens_products_page(page: Page) -> None:
    """A valid demo login should open the products page."""
    login(page, USERNAME, PASSWORD)

    expect(page).to_have_url(re.compile(r".*/inventory\.html(?:\?.*)?$"))
    expect(page.locator(".title")).to_have_text("Products")
    expect(page.locator(".inventory_item").first).to_be_visible()


def test_add_product_to_cart(page: Page) -> None:
    """A user should be able to add a product and see it in the cart."""
    login(page, USERNAME, PASSWORD)
    expect(page.locator(".title")).to_have_text("Products")

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    page.locator(".shopping_cart_link").click()
    expect(page).to_have_url(re.compile(r".*/cart\.html(?:\?.*)?$"))
    expect(page.locator(".cart_item")).to_have_count(1)
    expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")


def test_invalid_login_displays_error(page: Page) -> None:
    """Invalid credentials should display a visible login error."""
    login(page, "invalid_user_for_portfolio_demo", "incorrect_password")

    error = page.locator('[data-test="error"]')
    expect(error).to_be_visible()
    expect(error).to_contain_text("Username and password do not match")
