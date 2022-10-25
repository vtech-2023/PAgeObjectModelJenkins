import logging

import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.InboxPage import InboxPage
from Pages.LoginPage import LoginPage
from TestCases.BaseTest import BaseTest
from Utilities import datareader
from Utilities.LogUtil import Logger

# from Utilities.datareader import getDataExcel

"""
1) To run multiple test cases in a specific order, install the package

pip install pytest-ordering

2) Refer the documentation -->https://pytest-ordering.readthedocs.io/en/develop/

"""


# def get_loginData():
# return [
#
#     ("selenium.testmay2017", "test@1234"),
#     ("selenium.testmay2017", "test@123"),
#     ("selenium.testmay201", "test@1234"),
#     ("selenium.testmay201", "test@123")
#
# ]
# return getDataExcel("LoginData")

log = Logger(__name__,logging.INFO)


class TestRediffmailSendMail(BaseTest):
    """
    Business Scenario:
        1) Send Mail  - starts with login, send mail and logout
        2) Create Account - Click on create account link, Fill the create account format
        3) Forgot Password - Click on Forgot password , create new password
        4) SaveMAil -  starts with login, save mail as draft and logout
        5) Trash -  starts with login, Click on Trash  and logout
    """

    # @pytest.mark.parametrize("username, password", get_loginData())

    @pytest.mark.parametrize("username, password,tofield, subjectarea, composetext",datareader.getDataExcel("SendMail"))
    def test_doRediffSendMail(self, username, password, tofield, subjectarea, composetext):
        print(username, "--", password, "--", tofield, "--", subjectarea, "--", composetext)
        l = LoginPage(self.driver)
        i = InboxPage(self.driver)
        l.loginSignedInChecked(username, password)
        log.logger.info("Test to Sign up finished - Send Mail")
        allure.attach(self.driver.get_screenshot_as_png(), name="RediffmailLogin", attachment_type=AttachmentType.PNG)
        allure.attach(self.driver.get_screenshot_as_png(), name="RediffmailLogin", attachment_type=AttachmentType.PNG)

        i.SendMail(tofield, subjectarea, composetext)
        log.logger.info("Test to send mail over")
        allure.attach(self.driver.get_screenshot_as_png(), name="RediffmailSendMail", attachment_type=AttachmentType.PNG)
        # Comment for print
        print("Finished  - running Send Email test Case")


    # @pytest.mark.run(order=2)
    # @pytest.mark.parametrize("tofield, subjectarea, composetext", datareader.getDataExcel("SendMail"))
    # def test_doRediffSendMail(self,tofield, subjectarea, composetext):
    #     i = InboxPage(self.driver)
    #     i.SendMail(tofield, subjectarea, composetext)
    #     allure.attach(self.driver.get_screenshot_as_png(), name="RediffmailSendMal", attachment_type=AttachmentType.PNG)
