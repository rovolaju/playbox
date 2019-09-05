from Page import Page


class Nav_Menu(Page):
    "Page object for the side menu"

    def start(self):
        "Xpath of all the field"
        # Navigation Menu
        self.inbox = "//a[contains(@href, '#inbox')]"
        self.sent_mail = "//a[contains(@href, '#sent')]"
        self.drafts = "//a[contains(@href, '#drafts')]"

    def select_menu_item(self, menu_item):
        "select menu item"