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


log = Logger(__name__,logging.INFO)


class TestRediffmailSaveMail(BaseTest):


    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("username, password,tofield, subjectarea, composetext",datareader.getDataExcel("SaveMail"))
    def test_doRediffSaveMail(self, username, password, tofield, subjectarea, composetext):

        print(username, "--", password, "--", tofield, "--", subjectarea, "--", composetext)
        l = LoginPage(self.driver)
        i = InboxPage(self.driver)
        l.loginSignedInChecked(username, password)
        log.logger.info("Test to Sign up finished - Save Mail")
        allure.attach(self.driver.get_screenshot_as_png(), name="RediffmailLogin", attachment_type=AttachmentType.PNG)


        i.SaveMail(tofield, subjectarea, composetext)
        log.logger.info("Test to save mail over")
        allure.attach(self.driver.get_screenshot_as_png(), name="RediffmailSaveMail", attachment_type=AttachmentType.PNG)
        # Comment for print
        print("Finished - running Save Email test Case")
