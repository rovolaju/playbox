def file_reader(file_location):
    file = open(file_location, "rt")
    content = file.readlines()
    file.close()
    return content


def screenshot(driver, save_location, url):
    filename: str = "_screen_" + url + ".png"
    driver.save_screenshot(save_location + filename)
