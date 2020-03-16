import re

from selenium import webdriver
from POM_Model.Tools import Utils as u
from POM_Model.Pages import Page_methods as p

test_urls = u.file_reader(p.Samples.sample_urls)

driver = webdriver.PhantomJS(executable_path='/Users/rdavila/Workspace/phantomjs-2.1.1-macosx/bin'
                                                          '/phantomjs')
i = 0
location = "/Users/rdavila/Workspace/playbox/POM_Model/screenshots/"
screen = ["", ""]
for url in test_urls:
    print(url)
    parsed_urls = p.Samples.parse_url(url)
    driver.set_window_size(1024, 768)
    driver.get(parsed_urls)
    url = re.sub(r'http\S+', '', url) + str(i)
    print(url)
    screen[i] = u.capture_screens(driver,
                                  location, url)
    i += 1
u.image_compare(screen[0], screen[1], location)

driver.close()
