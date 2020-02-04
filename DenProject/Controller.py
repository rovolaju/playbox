import re


def format_raw_content(content):

    pass


def get_url_list():
    file = open("url_sample.txt", "r")
    content = file.read()
    print(content)
    #need function to clean up whatever conntets of the base urls filw
    #format_raw_content(content)
    return content


def grab_image():
    pass


def trigger(content):
    for url in content:
        grab_image()
        




something = get_url_list()
