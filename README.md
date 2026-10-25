# UI and API Test Automation Suite

Playwright page-object tests for login, cart, checkout and error handling alongside Requests API tests. A deterministic local shop supports offline CI; browser traces/screenshots and pytest HTML reports are retained on failure.

## Run

Install requirements.txt and `playwright install chromium`. Run `pytest --tracing=retain-on-failure --screenshot=only-on-failure --html=report.html`. Fixtures start the bundled demo. The local demo accepts standard_user/secret_sauce.
