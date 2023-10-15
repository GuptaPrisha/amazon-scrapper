from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
from pprint import pprint

PATH = r"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

links = []
driver.get("https://www.amazon.in/")
products = {}

search = driver.find_element(By.ID, "twotabsearchtextbox")
searchButton = driver.find_element(By.ID, "nav-search-submit-button")

search.send_keys("smartphones")
time.sleep(3)
searchButton.click()
for i in range(1):
    print("product", i + 1)
    mobiles = driver.find_elements(
        By.XPATH,
        "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']",
    )
    for mobile in mobiles:
        links.append(mobile.get_attribute("href"))

products["data"] = links
jsonStr = json.dumps(products)
# print(jsonStr)

with open("./link.json", "a") as f:
    f.write(jsonStr)


# mobile.click()
# time.sleep(2)
# title = driver.find_element(By.XPATH, "//span[@id='productTitle']")
# print(title)
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price)
# driver.back()
