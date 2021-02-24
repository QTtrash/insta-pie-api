from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os

options = Options()
options.headless = True


def get_following(username, login, password):
    browser = webdriver.Firefox(
        options=options, service_log_path=os.path.devnull)
    # Depends on internet connections
    browser.implicitly_wait(5)

    print("Initialising browser...\n")
    print("Connecting to instagram.com...\n")
    browser.get('https://www.instagram.com/')

    sleep(2)

    print("Accepting Cookies...\n")
    accept_cookies_button = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div[2]/button[1]')
    accept_cookies_button.click()

    sleep(2)

    print("Searching for input field...\n")
    username_input = browser.find_element_by_css_selector(
        "input[name='username']")
    password_input = browser.find_element_by_css_selector(
        "input[name='password']")

    print("Writing in your data...\n")
    username_input.send_keys(login)
    password_input.send_keys(password)

    sleep(0.5)

    print("Clicking submit...\n")
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    sleep(3)

    print("Connecting to user's page...")
    browser.get("https://www.instagram.com/{}/".format(username))

    print("Clicking following...")
    following_num = browser.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
    following_num.click()

    print("getting following list...")
    following_list = "document.getElementsByClassName('isgrP')[0]"

    last_height = browser.execute_script(
        "return {}.scrollHeight".format(following_list))
    while True:
        browser.execute_script(
            "{}.scrollTo(0, {}.scrollHeight);".format(following_list, following_list))

        sleep(1.5)

        new_height = browser.execute_script(
            "return {}.scrollHeight".format(following_list))
        if new_height == last_height:
            break
        last_height = new_height

    following = browser.find_elements_by_class_name("FPmhX")
    print(len(following))
    id = 0
    json_result = {"following": []}
    for following_user in following:
        name = following_user.get_attribute('title')
        link = "instagram.com/{}".format(name)
        following_object = {
            "following_id": id,
            "name": name,
            "link": link
        }
        json_result["following"].append(following_object)
        id += 1

    return json_result