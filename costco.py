# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import requests
# Chromedriver(in codebase)
service = Service(executable_path="chromedriver.exe")
# Setting up driver
driver = webdriver.Chrome(service=service)
time.sleep(5)
#Setting up arrays
links_array = ["https://www.costco.com/2024-1-oz-American-Eagle-Gold-Coin.product.1804545.html", "https://www.costco.com/1-oz-Gold-Bar-PAMP-America-the-Free-Statue-of-Liberty-(New-in-Assay).product.1814004.html"]
#Telegram key/setup
TOKEN = "XXX"
chat_id = "XXX"
not_found_counter = 0
index_counter = 0
while links_array:
    driver = webdriver.Chrome(service=service)
    driver.get(links_array[index_counter])
    time.sleep(2)
    try:
        driver.find_element(By.ID, "not_found_body")
    except NoSuchElementException:
        not_found_counter += 1
            # container = driver.find_element(By.CLASS_NAME, "col-xs-12")
            # cont_guide = container.find_element(By.CLASS_NAME, "crumbs")
    if not_found_counter == 0:
        print("Hello World!")
        message = links_array[index_counter]
        url = f"https://v1.nocodeapi.com/thebotfather/telegram/ItHIluRtWvbAlbbp/sendText?text={message}"
        params = {}
        time.sleep(3)
        r = requests.post(url = url, params = params)
        driver.quit()
        index_counter += 1
        links_array.remove(links_array[index_counter])
    else:
        driver.quit()
        driver.get(links_array[index_counter])
        

        