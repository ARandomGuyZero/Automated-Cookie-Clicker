"""
Automated Cookie Clicker

Author: Alan
Date: October 5th 2024

Automatically plays the Cookie Clicker game for five minutes.
"""

from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://orteil.dashnet.org/experiments/cookie/"

# Gets new webdriver object
driver = webdriver.Chrome()

# Gets the data from the driver
driver.get(url=URL)

# Gets the cookie item (the one we will click)
cookie = driver.find_element(By.ID, value="cookie")

# Gets the amount of cookies
cookie_amount = driver.find_element(By.ID, value="money")

# Get a list of items of the in-game store
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")

# Store the items in an item list by getting their id attribute
store_items = [item.get_attribute("id") for item in items]

# Start the game timer
game_time = time()

# This game will run for 5 minutes
while time() - game_time < 60 * 5:

    start_time = time()

    # For five seconds, we will buy as many cookies as possible
    while time() - start_time < 5:

        cookie.click()

    # Once 5 seconds have passed, we try to buy some stuff
    for item_name in store_items[::-1]:

        # There's not currently an Elder Pledge, so there's no reason to get it
        if not item_name == "buyElder Pledge":
            # Get an element of the list of elements
            item = driver.find_element(By.ID, value=item_name)

            # Get the cost of the item to integer
            item_cost = int(item.text.strip().split(" - ")[1].split("\n")[0].replace(",", ""))

            # Format the amount of cookies to integer
            cookies = int(cookie_amount.text.replace(",", ""))

            # Checks if we can afford the price, if we can, we buy
            if cookies >= item_cost:
                item.click()
                break

# Gets the amount of cookies per second
cookies_second = driver.find_element(By.ID, value="cps")
print(cookies_second.text)
