# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from deep_translator import GoogleTranslator
import time
import requests
# Chromedriver(in codebase)
service = Service(executable_path="chromedriver.exe")
# Setting up driver
driver = webdriver.Chrome(service=service)
translator = GoogleTranslator(source='auto', target='en')
driver.get("https://www.uscardforum.com/c/rewards/12")
time.sleep(5)
arr = []
res = []
links = []
old_titles = []
compare = []
#Telegram key/setup
TOKEN = "XXX"
chat_id = "XXX"
titles = driver.find_elements(By.CLASS_NAME, "title")
for i in range(5):
    arr.append(translator.translate(titles[i].text))
while True:
    time.sleep(1)
    driver.quit()
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.uscardforum.com/c/rewards/12")
    time.sleep(5)
    titles2 = driver.find_elements(By.CLASS_NAME, "title")
    for i in range(5):
        compare.append(translator.translate(titles2[i].text))
    for n in compare:
        if n not in arr and n not in old_titles:
                res.append(n)
    for i in titles2:
         links.append(i.get_attribute('href'))
    if res:
        print("hello")
        string = ""
        for i in res:
            string = string + "" + i + f" ({links[compare.index(i)]}) "
        message = "Hi, here are the following updates📤: " + string
        url = f"https://v1.nocodeapi.com/thebotfather/telegram/ItHIluRtWvbAlbbp/sendText?text={message}"
        params = {}
        time.sleep(3)
        r = requests.post(url = url, params = params)
        # url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        # time.sleep(3)
        # print(requests.get(url).json()) # this sends the messages
        old_titles.extend(res)
        res.clear()

    compare.clear()
    message = ""
    string = ""
