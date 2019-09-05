def get_page_object(page_name, driver, base_url='https://gmail.com/'):
    "Return the appropriate page object based on page_name"
    test_obj = None
    page_name = page_name.lower()
    if page_name == "login":
        test_obj = Login_Page(driver, base_url=base_url)
    elif page_name == "main":
        test_obj = Main_Page(driver, base_url=base_url)

    return test_obj