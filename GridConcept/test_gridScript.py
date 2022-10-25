import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
Sequential Testing
1)pytest test_gridScript.py -s -v --alluredir="C:/Users/lenovo/Desktop/SeleniumPython/Workspace_VTech/GridConcept/allurereports"

Parallel Testing - need pytest-xdist package to be installed
1)pytest test_gridScript.py -s -v -n 8 --alluredir="C:/Users/lenovo/Desktop/SeleniumPython/Workspace_VTech/GridConcept/allurereports"

Open command prompt and fire to create allure reports:
allure serve C:/Users/lenovo/Desktop/SeleniumPython/Workspace_VTech/GridConcept/allurereports
"""


@pytest.fixture()
def log_on_failure(request, get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="GridFailure", attachment_type=AttachmentType.PNG)


def get_loginData():
    return [

        ("selenium.testmay2017", "test@1234"),
        ("selenium.testmay2017", "test@123"),
        ("selenium.testmay201", "test@1234"),
        ("selenium.testmay201", "test@123")

    ]


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("username, password", get_loginData())
def test_doRediffloginGrid(username, password, get_browser):
    driver = get_browser
    driver.implicitly_wait(100)
    # Username field
    driver.find_element(By.ID, "login1").send_keys(username)
    time.sleep(2)
    # Password field
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(2)
    # Signin buttoon
    driver.find_element(By.NAME, "proceed").submit()
    time.sleep(2)
    assert 1 == 2
    allure.attach(driver.get_screenshot_as_png(), name="test_doRediffloginGrid", attachment_type=AttachmentType.PNG)
