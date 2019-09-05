class Page(unittest.TestCase):
    #Master page class

    def __init__(self, selenium_driver, base_url='https://mail.google.com/'):
        #Constructor
        if base_url[-1] != '/':
            base_url += '/'
        self.base_url = base_url
        self.driver = selenium_driver
        # Visit and initialize xpaths for the appropriate page
        self.start()
        # Initialize the logger object
        self.log_obj = Base_Logging(level=logging.DEBUG)

    def open(self, url):
        "Visit the page base_url + url"
        url = self.base_url + url
        self.driver.get(url)

    def get_xpath(self, xpath):
        "Return the DOM element of the xpath OR the 'None' object if the element is not found"

    def click_element(self, xpath):
        "Click the button supplied"

    def write(self, msg, level='info'):
        self.log_obj.write(msg, level)

    def wait(self, wait_seconds=5):
        " Performs wait for time provided"
        time.sleep(wait_seconds)