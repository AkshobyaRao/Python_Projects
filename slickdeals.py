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
message = ""
driver = webdriver.Chrome(service=service)
translator = GoogleTranslator(source='auto', target='en')
driver.get("https://slickdeals.net/live/")
time.sleep(5)
titles = []
links = []
upvotes = []
compare = []
res = []
old_titles = []
#Telegram key/setup
TOKEN = "XXX"
chat_id = "XXX"
p1 = driver.find_element(By.ID, "liveview_post_container")
p2 = p1.find_elements(By.CLASS_NAME, "liveview_post_box")
for i in p2:
     p3 = i.find_element(By.CLASS_NAME, "liveview_thumbs")
     uv = p3.find_element(By.CSS_SELECTOR, "span")
     upvotes.append(uv.text)
     content = i.find_element(By.CLASS_NAME, "liveview_post_box_content")
     ttl = content.find_elements(By.CSS_SELECTOR, "a")
     for i in ttl[0:10]:
        if i.text != "Hot Deals":   
            print(i.text)
            titles.append(i.text)
            links.append(i.get_attribute('href'))

driver.quit()
time.sleep(3)
for i in links[0:5]:
     driver = webdriver.Chrome(service=service)
     driver.get(i)
     cont = driver.find_element(By.CLASS_NAME, "dealScoreBox")
     cont = cont.text
     cont = cont.replace("+", "")
     cont = cont.replace(" ", "")
     compare.append(cont)
     if abs(int(compare[links.index(i)])) > 0 and abs(int(compare[links.index(i)])) >= abs(int(upvotes[links.index(i)])) and titles[(links.index(i))] not in old_titles:
          res.append(f'{titles[links.index(i)]}({i})')
          old_titles.append(titles[links.index(i)])
     else:
          print(titles[links.index(i)])
          titles.remove(titles[links.index(i)])
          upvotes.remove(upvotes[links.index(i)])
          links.remove(i)

     driver.quit()
     time.sleep(3)

if res:
        print("hello3")
        string = ""
        for i in res:
            string = string + ' ' + i 
        message = "Hi, here are the following updates📤: " + string
        url = f"https://v1.nocodeapi.com/thebotfather/telegram/ItHIluRtWvbAlbbp/sendText?text={message}"
        params = {}
        time.sleep(3)
        r = requests.post(url = url, params = params)
        # url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        # time.sleep(3)
        # print(requests.get(url).json()) # this sends the messages
        res.clear()

message = ""
string = ""
