# Browser Automation & Testing with Playwright

## Overview

This portfolio project demonstrates browser-based functional testing with Python, Playwright, and pytest against the public SauceDemo test storefront.

Example scenarios:
- Verify the login form is visible.
- Log in with demo credentials and verify the products page.
- Add a product to the cart and verify the cart contents.
- Submit invalid credentials and verify the error message.

These are example tests for a public demo site. They do not claim to test an employer's systems.

## Tools

- Python
- Playwright
- pytest and pytest-playwright
- Chromium
- GitHub Actions

## Project files

- `test_browser_automation.py` — four example functional tests.
- `requirements.txt` — Python dependencies.
- `TEST-RESULTS.md` — recorded local test results.
- `.github/workflows/playwright-tests.yml` — CI workflow that runs the tests on pushes and pull requests and can also be started manually.

## Local setup (Windows PowerShell)

Open PowerShell in the folder containing these files, then run:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -v
```

`pytest-playwright` supplies the built-in `page` fixture used by the tests.

## Continuous integration with GitHub Actions

The workflow at `.github/workflows/playwright-tests.yml`:
1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs the Python dependencies.
4. Installs Chromium and its system dependencies.
5. Runs `python -m pytest -v`.

It is configured to run on pushes, pull requests, and manual dispatch (`workflow_dispatch`). A successful workflow run means the job completed without a reported failure. To confirm individual test results, open the run in the GitHub **Actions** tab and inspect the **Run browser tests** step and its pytest summary.

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

## Recorded results

The local run recorded in `TEST-RESULTS.md` reported **4 passed in 2.65 seconds** on Windows with Python 3.14.8, pytest 9.1.1, and Chromium.

The first GitHub Actions workflow run was also observed as successful in the repository's Actions page. The exact CI test count should be confirmed in that run's `Run browser tests` step before reporting it as a separate result.

## Quality practices demonstrated

- Arrange / act / assert.
- Assertions for visible controls, navigation, and cart contents.
- Reusable login helper.
- Environment-variable configuration.
- Positive and negative-path testing.
- CI execution on pushes and pull requests.

## Limitations

This is a learning/portfolio example, not a comprehensive test suite. It depends on an external public demo site and does not test production systems, performance, security, or accessibility. Results may vary if the demo site changes.
