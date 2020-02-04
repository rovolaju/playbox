from selenium import webdriver
import re

file = open("url_sample.txt", "rt")
content = file.readlines()
driver = webdriver.Safari()
#print(content)

for url in content:
    parsedurl=str(url.strip())
    print(parsedurl)

    #driver.maximize_window()
    driver.get(parsedurl)
    filename= "screen_"+re.search("^www.$",parsedurl)+".png"
    print(re.search("^www.$",parsedurl))
    print(filename)
    driver.save_screenshot(filename)
driver.close()
file.close()