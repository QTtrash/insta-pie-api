import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

options = Options()
options.headless = True


# Headless because there is still nothing to show to HR
def get_user(username):
    browser = webdriver.Firefox(
        options=options, service_log_path=os.path.devnull)
    # Depends on internet connections
    browser.implicitly_wait(3)

    print("Connecting to user's page...\n")
    browser.get("https://www.instagram.com/{}/".format(username))

    print("Accepting Cookies...\n")
    accept_cookies_button = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div[2]/button[1]')
    accept_cookies_button.click()

    print("Getting the provided name of the user...")
    name = "NO NAME PROVIDED"
    if browser.find_elements_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/h1"):
        name = browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/div[2]/h1").get_attribute("innerHTML")
        print("Provided name: " + name + "\n")

    print("Getting number of posts...")
    number_of_posts = "0"
    if(browser.find_elements_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[1]/a/span")):
        number_of_posts = browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[1]/a/span").get_attribute("innerHTML")
        print("Number of posts: " + number_of_posts + "\n")

    print("Getting number of followers...")
    number_of_followers = "0"
    if(browser.find_elements_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")):
        number_of_followers = browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").get_attribute("innerHTML")
        print("Number of followers: " + number_of_followers + "\n")

    print("Getting number of users followed...")
    number_of_following = "0"
    if(browser.find_elements_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span")):
        number_of_following = browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").get_attribute("innerHTML")
        print("Number of users followed: " + number_of_following + "\n")

    description = "NO DESCRIPTION PROVIDED"
    if browser.find_elements_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/span"):
        print("Getting user\'s description...")
        description = browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/div[2]/span").get_attribute("innerHTML")
        print("Description: \n\t" + description.replace("<br>", "\n\t") + "\n")

    user = {
        "username": username,
        "name": name,
        "posts": number_of_posts,
        "followers": number_of_followers,
        "following": number_of_following,
        "description": description
    }

    print(json.dumps(user, indent=4))

    browser.close()
    return user


def get_user_group(usernames):

    user_group = {
        "users": []
    }

    browser = webdriver.Firefox(
        options=options, service_log_path=os.path.devnull)
    # Depends on internet connections
    browser.implicitly_wait(3)

    for username in usernames:
        if(username == "" or username.startswith(">") or username.startswith("<")):
            continue
        elif(username.startswith('@')):
            username = username[1:]
        elif(username.startswith('https')):
            username = username[27:]

        print("Connecting to user's page...\n")
        browser.get("https://www.instagram.com/{}/".format(username))

        print("Accepting Cookies...\n")
        if(browser.find_elements_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')):
            accept_cookies_button = browser.find_element_by_xpath(
                '/html/body/div[2]/div/div/div/div[2]/button[1]')
            accept_cookies_button.click()

        if(browser.find_elements_by_xpath('/html/body/div[1]/section/main/div/h2')):
            print("Skipping broken link")
            continue

        print("Getting the provided name of the user...")
        name = "NO NAME PROVIDED"
        if browser.find_elements_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/h1'):
            name = browser.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/div[2]/h1").get_attribute("innerHTML")
            print("Provided name: " + name + "\n")

        print("Getting number of posts...")
        number_of_posts = "0"
        if(browser.find_elements_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[1]/a/span")):
            number_of_posts = browser.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[1]/a/span").get_attribute("innerHTML")
            print("Number of posts: " + number_of_posts + "\n")

        print("Getting number of followers...")
        number_of_followers = "0"
        if(browser.find_elements_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")):
            number_of_followers = browser.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").get_attribute("innerHTML")
            print("Number of followers: " + number_of_followers + "\n")

        print("Getting number of users followed...")
        number_of_following = "0"
        if(browser.find_elements_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span")):
            number_of_following = browser.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").get_attribute("innerHTML")
            print("Number of users followed: " + number_of_following + "\n")

        description = "NO DESCRIPTION PROVIDED"
        if browser.find_elements_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/span"):
            print("Getting user\'s description...")
            description = browser.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/div[2]/span").get_attribute("innerHTML")
            print("Description: \n\t" + description.replace("<br>", "\n\t") + "\n")

        user = {
            "username": username,
            "name": name,
            "posts": number_of_posts,
            "followers": number_of_followers,
            "following": number_of_following,
            "description": description
        }

        print(json.dumps(user, indent=4))

        user_group["users"].append(user)

    browser.close()
    return user_group
