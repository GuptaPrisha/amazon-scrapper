from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json

PATH = r"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

links = [
    "DealContent-module__truncate_sWbxETx42ZPStTc9jwySW",
    "DealContent-module__truncate_sWbxETx42ZPStTc9jwySW",
    "DealContent-module__truncate_sWbxETx42ZPStTc9jwySW",
    "DealContent-module__truncate_sWbxETx42ZPStTc9jwySW",
    "DealContent-module__truncate_sWbxETx42ZPStTc9jwySW",
]
driver.get("https://www.amazon.in/")
products = []

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Today's Deals"))
    )
    element.click()
    for i in links:
        wait = WebDriverWait(driver, 10)
        mobile = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, i)))
        mobile.click()
        print("mobile clicked successfully")
        mobile = {}
        try:
            title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "productTitle"))
            )
            reviewers = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, "acrCustomerReviewText"))
            )
            # rating = driver.find_element(By.CLASS_NAME, "a-size-base a-color-base")
            # print(rating.text)
            price = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, "a-list-item"))
            )
            # brand = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, "a-size-base po-break-word"))
            # )
            # print("brand")

            mobile["title"] = title.text
            mobile["reviewers"] = reviewers.text
            mobile["info"] = price.text

            products.append(mobile)
            driver.back()
        except:
            driver.back()
            print("unsuccessful")

except:
    driver.quit()

print(products)

jsonStr = json.dumps(products)
print(jsonStr)

with open("./new.json", "a") as f:
    f.write(jsonStr)
