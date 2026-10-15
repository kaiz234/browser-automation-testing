# Browser Automation & Testing with Playwright

## Overview

This portfolio project demonstrates browser-based functional testing with Python and Playwright. It uses a public demo storefront so the test flow can be demonstrated without exposing employer systems, internal URLs, credentials, or production data.

The sample tests cover:
- Opening the demo application and checking that the login page is visible.
- Logging in with demo credentials and checking successful navigation.
- Adding an item to the cart and verifying the cart contents.
- Submitting invalid credentials and checking that an error is displayed.

**Important:** These are example automated tests for a public demo site. They do not claim to be tests executed against BAC or any employer system.

## Tools

- Python
- Playwright for Python
- pytest
- Environment variables for optional credential overrides

## Project files

- `test_browser_automation.py` — example functional tests.
- `requirements.txt` — Python dependencies.
- `README.md` — setup, execution, and interpretation notes.

## Setup

Use Python 3.10 or later.

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install dependencies and browser binaries:

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Run the tests

```bash
python -m pytest -v
```

To use different demo credentials, set environment variables before running. Do not commit real credentials.

PowerShell:

```powershell
$env:DEMO_USERNAME = "standard_user"
$env:DEMO_PASSWORD = "secret_sauce"
python -m pytest -v
```

macOS / Linux:

```bash
export DEMO_USERNAME="standard_user"
export DEMO_PASSWORD="secret_sauce"
python -m pytest -v
```

The example uses the public SauceDemo test site. Its availability, behavior, and demo credentials are controlled by that service and may change.

## Test scenarios

| Test | Purpose | Expected result |
|---|---|---|
| Login page loads | Check that the expected login controls appear | Username and password fields are visible |
| Valid login | Confirm the demo user can sign in | Products page appears |
| Add product to cart | Check a common shopping workflow | Cart badge and selected item are visible |
| Invalid login | Check basic error handling | An error message appears |

## Quality practices demonstrated

- Arrange / act / assert test structure.
- Explicit assertions instead of relying only on successful clicks.
- Reusable fixtures for browser and page setup.
- Environment-variable configuration for credentials.
- Negative-path testing.
- Clear test names and failure output.

## Troubleshooting

- **Browser executable missing:** run `python -m playwright install chromium`.
- **Dependency import errors:** activate the virtual environment and run `python -m pip install -r requirements.txt`.
- **Timeout or selector failure:** confirm the demo site is available and inspect the current page markup; the site's UI may have changed.
- **Unexpected login result:** verify the demo credentials published by the demo service. Do not work around access controls or use real account credentials.
- **Headless/browser differences:** run pytest with `--headed` to observe the browser when debugging.

## Limitations

- This is a learning/portfolio example, not a comprehensive test suite.
- The sample depends on an external public demo site.
- It does not test production systems, performance, security, or accessibility.
- No pass rate or test execution result is claimed until the tests are run and the actual output is recorded.

## Future improvements

- Add a GitHub Actions workflow to run the suite on pushes and pull requests.
- Publish a sanitized test report as a CI artifact.
- Add API-level checks and more negative test cases.
- Use page objects if the suite grows.
