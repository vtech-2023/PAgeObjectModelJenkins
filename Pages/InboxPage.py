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
        self.StaticWait(2)
        self.EnterButtonEditBoxEmail("toField_XPATH")
        self.StaticWait(2)
        self.TypeEditBox("subject_XPATH", subjectarea)
        self.StaticWait(2)
        self.SwitchFrameAddress("frameCompose_CSSSELECTOR")
        self.StaticWait(2)
        self.TypeEditBox("composeArea_XPATH", composetext)
        self.StaticWait(2)
        self.SwitchOutFrameAddress()
        self.StaticWait(2)
        self.ClickLinks("send_XPATH")
        self.StaticWait(2)
        self.ClickLinks("logout_XPATH")
        self.StaticWait(2)

    def SaveMail(self, tofield, subjectarea, composetext):
        self.DynamicImplicitWait(100)
        self.ClickLinks("writeMail_XPATH")
        self.StaticWait(6)
        self.TypeEditBox("TO_IDcmp2", tofield)
        self.StaticWait(2)
        self.EnterButtonEditBoxEmail("TO_IDcmp2")
        self.StaticWait(2)
        self.TypeEditBox("subject_XPATH", subjectarea)
        self.StaticWait(2)
        self.SwitchFrameAddress("frameCompose_CSSSELECTOR")
        self.StaticWait(2)
        self.TypeEditBox("composeArea_XPATH", composetext)
        self.StaticWait(2)
        self.SwitchOutFrameAddress()
        self.StaticWait(2)
        self.ClickLinks("save_XPATH")
        self.StaticWait(2)
        self.ClickLinks("logout_XPATH")
        self.StaticWait(2)
