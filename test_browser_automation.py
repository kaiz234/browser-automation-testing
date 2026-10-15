"""Example browser functional tests using pytest and Playwright."""

import os

import pytest
from playwright.sync_api import Page, expect

BASE_URL = os.getenv("DEMO_BASE_URL", "https://www.saucedemo.com/")
USERNAME = os.getenv("DEMO_USERNAME", "standard_user")
PASSWORD = os.getenv("DEMO_PASSWORD", "secret_sauce")


@pytest.fixture
def app(page: Page) -> Page:
    """Open the demo application before each test."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    return page


def login(page: Page, username: str, password: str) -> None:
    """Submit the demo application's login form."""
    page.locator('[data-test="username"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[data-test="login-button"]').click()


def test_login_page_displays_expected_fields(app: Page) -> None:
    """The login page should show the username, password, and login controls."""
    expect(app.locator('[data-test="username"]')).to_be_visible()
    expect(app.locator('[data-test="password"]')).to_be_visible()
    expect(app.locator('[data-test="login-button"]')).to_be_visible()


def test_valid_login_opens_products_page(app: Page) -> None:
    """A valid demo login should open the products page."""
    login(app, USERNAME, PASSWORD)

    expect(app).to_have_url("**/inventory.html")
    expect(app.locator(".title")).to_have_text("Products")
    expect(app.locator(".inventory_item").first).to_be_visible()


def test_add_product_to_cart(app: Page) -> None:
    """A user should be able to add a product and see it in the cart."""
    login(app, USERNAME, PASSWORD)

    expect(app.locator(".title")).to_have_text("Products")
    app.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    expect(app.locator(".shopping_cart_badge")).to_have_text("1")
    app.locator(".shopping_cart_link").click()

    expect(app).to_have_url("**/cart.html")
    expect(app.locator(".cart_item")).to_have_count(1)
    expect(app.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")


def test_invalid_login_displays_error(app: Page) -> None:
    """Invalid credentials should display a visible login error."""
    login(app, "invalid_user_for_portfolio_demo", "incorrect_password")

    error = app.locator('[data-test="error"]')
    expect(error).to_be_visible()
    expect(error).to_contain_text("Username and password do not match")
