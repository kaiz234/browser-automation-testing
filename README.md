# Browser Automation & Testing with Playwright

## Overview

This portfolio project demonstrates browser-based functional testing with Python, Playwright, and pytest against the public SauceDemo test storefront.

Example scenarios:
- Verify the login form is visible.
- Log in with demo credentials and verify the products page.
- Add a product to the cart and verify the cart contents.
- Submit invalid credentials and verify the error message.

These are example tests for a public demo site. They do not claim to test an employer's systems.

## Files

- `test_browser_automation.py` — four example functional tests.
- `requirements.txt` — Python dependencies.

## Setup (Windows PowerShell)

Open PowerShell in the folder containing these files, then run:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -v
```

`pytest-playwright` supplies the built-in `page` fixture. The tests use regular-expression URL assertions so they check the URL suffix rather than treating a glob-like string as an exact URL.

## Optional configuration

The defaults use the public demo site's standard test account. You can override them with environment variables; do not commit real credentials.

```powershell
$env:DEMO_BASE_URL = "https://www.saucedemo.com/"
$env:DEMO_USERNAME = "standard_user"
$env:DEMO_PASSWORD = "secret_sauce"
python -m pytest -v
```

## Test scenarios

| Test | Expected result |
|---|---|
| Login page displays expected fields | Username, password, and login controls are visible |
| Valid login opens products page | Products page and product listing appear |
| Add product to cart | Cart badge shows one item and cart contains the selected product |
| Invalid login displays error | A visible login error is shown |

## Quality practices demonstrated

- Arrange / act / assert.
- Assertions for visible controls, navigation, and cart contents.
- Reusable login helper.
- Environment-variable configuration.
- Positive and negative-path testing.

## Troubleshooting

- **`fixture 'page' not found`:** run `python -m pip install -r requirements.txt`.
- **Browser executable missing:** run `python -m playwright install chromium`.
- **Timeout or selector failure:** check the demo site and current page markup; site behavior may change.
- **Unexpected login result:** check the public demo site's availability and credentials.

## Limitations

This is a learning/portfolio example, not a comprehensive test suite. It depends on an external public demo site and should not be described as passing until a real run completes successfully. It does not test production systems, performance, security, or accessibility.
