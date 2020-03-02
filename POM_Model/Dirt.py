from selenium import webdriver
from POM_Model.Tools import Utils as u
from POM_Model.Pages import Page_methods as p


test_urls = u.file_reader(p.Samples.sample_urls)

driver = webdriver.Safari()

for url in test_urls:
    print(url)
    parsed_urls = p.Samples.parse_url(url)
    driver.maximize_window()
    driver.get(parsed_urls)
    u.screenshot(driver, "/Users/rdavila/Workspace/playbox/POM_Model/screenshots/", url)

driver.close()

