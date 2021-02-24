from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os

options = Options()
options.headless = True


def get_images(username):
    browser = webdriver.Firefox(
        options=options, service_log_path=os.path.devnull)
    # Depends on internet connections
    browser.implicitly_wait(5)

    print("Connecting to user's page")
    browser.get("https://www.instagram.com/{}/".format(username))

    print("Accepting Cookies...\n")
    accept_cookies_button = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div[2]/button[1]')
    accept_cookies_button.click()

    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        sleep(1.5)

        new_height = browser.execute_script(
            "return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    images = browser.find_elements_by_css_selector("img")
    id = 0
    json_result = {"images": []}
    for image in images:
        image_object = {
            "image_id": id,
            "alt": image.get_attribute('alt'),
            "src": image.get_attribute('src')
        }
        json_result["images"].append(image_object)
        id += 1

    return json_result
