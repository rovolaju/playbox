from selenium import webdriver

driver = webdriver.Safari()
driver.get("https://www.consumeraffairs.com/about/privacy_policy/")
element = driver.find_element_by_xpath("//a[text()='FAQ']")
print(element.__sizeof__())
#print(len(element))
print (element.text)
print (element.get_attribute("href"))

element.click()

driver.close()