from Pages.Base import BaseSettingsPage


class InboxPage(BaseSettingsPage):

    def __init__(self, driver):
        super().__init__(driver)

    def SendMail(self, tofield, subjectarea, composetext):
        self.DynamicImplicitWait(100)
        # self.DynamicExplcitWait("writeMail_XPATH", 20)
        # Assert the title
        self.AssertTitle("Rediffmail")
        self.AssertText("writeMailText_XPATH", "Write mail")
        self.StaticWait(2)
        self.ClickLinks("writeMail_XPATH")
        self.StaticWait(6)
        self.TypeEditBox("toField_XPATH", tofield)
        self.EnterButtonEditBoxEmail("toField_XPATH")
        self.TypeEditBox("subject_XPATH", subjectarea)
        self.SwitchFrameAddress("frameCompose_CSSSELECTOR")
        self.TypeEditBox("composeArea_XPATH", composetext)
        self.SwitchOutFrameAddress()
        self.ClickLinks("send_XPATH")
        self.ClickLinks("logout_XPATH")

    def SaveMail(self, tofield, subjectarea, composetext):
        self.DynamicImplicitWait(100)
        self.ClickLinks("writeMail_XPATH")
        self.StaticWait(6)
        self.TypeEditBox("toField_XPATH", tofield)
        self.EnterButtonEditBoxEmail("toField_XPATH")
        self.TypeEditBox("subject_XPATH", subjectarea)
        self.SwitchFrameAddress("frameCompose_CSSSELECTOR")
        self.TypeEditBox("composeArea_XPATH", composetext)
        self.SwitchOutFrameAddress()
        self.ClickLinks("save_XPATH")
        self.ClickLinks("logout_XPATH")
