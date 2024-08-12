# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Chromedriver(in codebase)
service = Service(executable_path="chromedriver.exe")
# Setting up driver
driver = webdriver.Chrome(service=service)

#Acessing Slickdeals.live
url = "https://slickdeals.net/live/"
driver.get(url)
time.sleep(2)
# Declaring arrays to compare old version of top 3 versus new version of top 3
new_top_five = []
rejected_top_five = []
#finding the titles and scores for each of the top 5(top 3 for now)
titles_top_five = {}
new_titles_top_five = []

upvotes_top_five = []
new_upvotes_top_five = []

links_top_five = []
new_links_top_five = []

def find_elements(web, link_arr, upvotes_arr, titles_dict_arr):
    top_five_containers = web.find_elements(By.CLASS_NAME, "liveview_vote_box")
    #Setting up base values for comparison
    for j in top_five_containers:
        top_five_containers_content = j.find_element(By.CLASS_NAME, "liveview_vote_box_content")
        #Finding links, upvotes, and titles
        link_title = top_five_containers_content.find_element(By.CSS_SELECTOR, "a")
        link_arr.append(link_title.get_attribute("href"))
        title = link_title.text
        if str(type(titles_dict_arr)) == "<class 'list'>":
             titles_dict_arr.append(title)
        else:
            titles_dict_arr[title] = 0
        new_titles_top_five.append(title)
        upvotes_container = top_five_containers_content.find_element(By.CSS_SELECTOR, "span")
        upvotes = upvotes_container.find_element(By.CSS_SELECTOR, "b").text
        upvotes_arr.append(upvotes)
#Calling func
find_elements(driver, links_top_five, upvotes_top_five, titles_top_five)
#Restarting driver
driver.quit()
new_driver = webdriver.Chrome(service=service)
new_driver.get(url)
time.sleep(2)
#Repeating previous base values to find differences
top_five_containers = new_driver.find_elements(By.CLASS_NAME, "liveview_vote_box")
#Setting up base values for comparison
find_elements(new_driver, new_links_top_five, new_upvotes_top_five, new_titles_top_five)
for i in range(5):
    print(new_titles_top_five[i])
    if new_titles_top_five[i] not in titles_top_five:
        titles_top_five[new_titles_top_five[i]] = 0
        rejected_top_five.append(new_titles_top_five[i])
        upvotes_top_five.append(new_titles_top_five[i])
        print("different" + new_titles_top_five[i])
        links_top_five.append(new_titles_top_five[i])
    else:
        print("same" + new_titles_top_five[i])
        titles_top_five[new_titles_top_five[i]] = int(titles_top_five[new_titles_top_five[i]]) + 1

new_titles_top_five.clear()      
# last step
for i in titles_top_five:
    if titles_top_five[i] > 0:
        new_top_five.append(i)
print(new_top_five)
