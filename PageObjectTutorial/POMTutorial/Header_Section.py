from Page import Page


class Header_Section(Page):
    "Page object for the page header"

    def start(self):
        "Xpath of all the fields"
        # Search and profile
        self.search_textbox = "//input[@id='gbqfq']"
        self.search_button = "//button[@id='gbqfb']"
        self.signout_button = "//a[text()='Sign out']"
        self.search_result = "//span[contains(text(),'%s')]"

    def search_by_subject(self, searchtext):
        self.set_text(self.search_textbox, 'subject:' + searchtext)

    