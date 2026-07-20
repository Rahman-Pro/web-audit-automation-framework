import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_configure(config):
    """Writes environment configuration metadata for Allure Reports."""
    allure_dir = config.getoption("--alluredir", default=None)
    if allure_dir and not os.path.exists(allure_dir):
        os.makedirs(allure_dir, exist_ok=True)
    if allure_dir:
        env_file = os.path.join(allure_dir, "environment.properties")
        with open(env_file, "w") as f:
            f.write("Browser=Headless Chrome\n")
            f.write("Platform=Ubuntu CI (GitHub Actions)\n")
            f.write("Framework=Pytest + Selenium WebDriver\n")
            f.write("Scope=12-Point Technical Audit\n")
            f.write("Author=Atiqur Rahman (SDET)\n")


@pytest.fixture(scope="function")
def driver(request):
    """Fixture to instantiate headless Chrome WebDriver."""
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(30)
    request.node.driver = driver

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot and attach to Allure Report upon test failure."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            try:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name=f"Failure_Screenshot_{item.name}",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception:
                pass
