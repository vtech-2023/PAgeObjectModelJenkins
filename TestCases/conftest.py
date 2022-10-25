import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
from Utilities import configreader


# This hook finds out if a test case has failed or passed or skipped
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request, get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Failure", attachment_type=AttachmentType.PNG)


@pytest.fixture(params=["firefox"], scope="function")
def get_browser(request):
    remote_url = "http://localhost:4444/wd/hub"
    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={"browserName": "chrome"})
    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={"browserName": "firefox"})
    request.cls.driver = driver

    # Maximise the browser window
    driver.maximize_window()
    # Page load timeout
    driver.set_page_load_timeout(200)
    # Navigate to URL
    driver.get(configreader.ConfigReader("base url", "URL"))

    yield driver
    time.sleep(2)
    driver.quit()
