from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
from progress.bar import FillingCirclesBar
from pprint import pprint
from pathlib import Path
import threading
from pymongo import MongoClient

with open("link.json", "r") as file:
    f = file.read()
    fd = json.loads(f)
    links = fd["data"]
data = {}
reviewLinks = {}
PATH = r"C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(PATH, options=options)
for link in links:
    driver.get(link)
    time.sleep(3)
    try:
        reviewButton = driver.find_element(
            By.XPATH,
            "//*[@id='reviews-medley-footer']/div[2]/a",
        )
        reviewLinks[link] = reviewButton.get_attribute("href")
    except:
        continue

    

data["data"] = reviewLinks
with open("reviewPage.json", "w+") as f:
    json.dump(data, f)

# "/html/body/div[2]/div/div[5]/div[25]/div/div/div/div/div/div[2]/div/div[2]/span[2]/div/div/div[3]/div[3]/div/div[2]/div/div/div[4]/span/div/div[1]/span"
