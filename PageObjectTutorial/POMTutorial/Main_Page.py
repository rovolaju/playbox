class Main_Page(Page):
    "Page object for the Main page"

    def start(self):
        self.url = ""
        self.open(self.url)
        # Create a Header Section object
        self.header_obj = Header_Section(self.driver)
        # Create a Menu object
        self.menu_obj = Nav_Menu(self.driver)