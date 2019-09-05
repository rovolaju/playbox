from Page import Page


class Login_Page(Page):
    "Page object for the Login page"

    def start(self):
        self.url = ""
        self.open(self.url)
        # Assert Title of the Login Page and Login
        self.assertIn("Gmail", self.driver.title)

        "Xpath of all the field"
        # Login
        self.login_email = "//input[@name='Email']"
        self.login_next_button = "//input[@id='next']"
        self.login_password = "//input[@placeholder='Password']"
        self.login_signin_button = "//input[@id='signIn']"

    def login(self, username, password):
        "Login using credentials provided"
        self.set_login_email(username)
        self.submit_next()
        self.set_login_password(password)
        self.submit_login()
        if 'Qxf2 Mail' in self.driver.title:
            self.write("Login Success")
            return True
        else:
            self.write("FAIL: Login error")
            return False

    def set_login_email(self, username):
        "Set the username on the login screen"

    def submit_next(self):
        self.click_element(self.login_next_button)
        self.wait(3)

    def set_login_password(self, password):
        "Set the password on the login screen"

    def submit_login(self):
        "Submit the login form"