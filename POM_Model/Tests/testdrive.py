from selenium import webdriver

driver = webdriver.Safari()
driver.get("https://www.google.com")
element = driver.find_element_by_xpath("//a[text()='About']")
print(element.__sizeof__())
#print(len(element))
print (element.text)
print (element.get_attribute("href"))

element.click()

driver.close()