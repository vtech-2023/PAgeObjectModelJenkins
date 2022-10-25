import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

# Grid based fixture
@pytest.fixture(params=["chrome","firefox"],scope="function")
def get_browser(request):
    remote_url = "http://localhost:4444/wd/hub"
    if request.param == "chrome":
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={"browserName": "chrome"})
    if request.param == "firefox":
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={"browserName": "firefox"})

    driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
    # Maximise the browser window
    driver.maximize_window()
    # Page load timeout
    driver.set_page_load_timeout(100)
    yield driver
    driver.quit()