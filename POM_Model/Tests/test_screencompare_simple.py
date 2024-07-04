import re

from selenium import webdriver
from POM_Model.Tools import Utils as Utility
from POM_Model.Pages import Page_methods as PageMethod

test_urls = Utility.file_reader(PageMethod.Samples.sample_urls)

driver = webdriver.PhantomJS(executable_path='/Users/rodrigodavila/PycharmProjects/phantomjs-2.1.1-macosx/bin'
                                                          '/phantomjs')
i = 0
location = "/Users/rodrigodavila/PycharmProjects/playbox/POM_Model/Pages/url_sample_"
screen = ["", ""]
for url in test_urls:
    print(url)
    parsed_urls = PageMethod.Samples.parse_url(url)
    driver.set_window_size(1024, 768)
    driver.get(parsed_urls)
    url = re.sub(r'http\S+', '', url) + str(i)
    print(url)
    screen[i] = Utility.capture_screens(driver,
                                        location, url)
    i += 1
Utility.image_compare(screen[0], screen[1], location)
Utility.analyze(screen[0], screen[1], location)

driver.close()
