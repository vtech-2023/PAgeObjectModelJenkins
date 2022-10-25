
# Will have all elements with their locators for the inbox page
# Methods to perform on the element

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.Base import BaseSettingsPage
from Pages.InboxPage import InboxPage
from Utilities import configreader


class LoginPage(BaseSettingsPage):

    def __init__(self, driver):
        super().__init__(driver)

    def loginSignedInChecked(self,username, password):

        # self.driver.get(configreader.ConfigReader("base url", "URL"))
        # self.driver.find_element_by_id(configreader.ConfigReader("locators", "username_ID")).send_keys("selenium.testmay2017")
        self.DynamicImplicitWait(100)
        # Assert the title
        self.AssertTitle("Rediffmail")
        # Assert by the text "Username"
        self.AssertText("usernaneText_XPATH", "Username")
        # Username Typed
        self.TypeEditBox("username_ID", username)
        # Password Typed
        self.TypeEditBox("password_ID", password)
        # Sign in Checkbox
        self.ClickCheckbox("signinCheckbox_NAME")
        # Sign in Button
        self.ClickButton("signinButton_NAME")
        self.StaticWait(5)


        # return InboxPage(self.driver)


    def forgotPassword(self):
        self.DynamicImplicitWait(100)
        # Link Clicked
        self.ClickLinks("forgotpassword_XPATH")

    def CreateAccount(self):
        self.DynamicImplicitWait(100)
        self.ClickLinks("createAccount_CSSSELECTOR")
