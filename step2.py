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
from fp.fp import FreeProxy

with open("./link.json", "r") as f:
    data = f.read()
    file = json.loads(data)
    allLinks = file["data"]

PATH = r"C:\Program Files (x86)\chromedriver.exe"

# try:
#     proxy = FreeProxy().get()
# except:
#     proxy = ""
proxy = ""
print(proxy)

# ----------------------------------------------------------------------------------------------


p = Path("./data")
p.mkdir(exist_ok=True)


def threadFunc(links, proxy, index):
    print(links)
    options = webdriver.ChromeOptions()
    # options.headless = True
    if proxy:
        options.add_argument(f"--proxy-server={proxy}")
    driver = webdriver.Chrome(PATH, options=options)

    productList = []
    with FillingCirclesBar("Processing", max=len(links)) as bar:
        for link in links:
            time.sleep(2)

            product = {}
            driver.get(link)

            title = WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.ID, "productTitle"))
            )
            product["title"] = title.text

            # c-family: condition ? true : false
            # python: true ? condition : false

            rating = driver.find_elements(
                By.XPATH, "//span[@class='a-size-base a-color-base']"
            )
            product["rating"] = rating[1].text if len(rating) > 2 else ""

            price = driver.find_elements(By.CLASS_NAME, "a-price-whole")
            product["price"] = price[4].text if len(price) > 5 else ""

            try:
                raters = driver.find_element(By.ID, "acrCustomerReviewText").text
                product["raters"] = int(raters.split(" ")[0])
            except:
                product["raters"] = 0

            img = driver.find_element(By.ID, "landingImage")
            product["imgSrc"] = img.get_attribute("src")

            info = driver.find_elements(By.CLASS_NAME, "a-list-item")
            if len(info) > 66:
                proInfo = []
                for i in info[61:65]:
                    proInfo.append(i.text)
                product["info"] = proInfo
            else:
                product["info"] = []

            productList.append(product)
            bar.next()

    pprint(productList)
    fileData = {}
    fileData["data"] = productList
    jsonStr = json.dumps(fileData)

    with open(f"./data/data-{index}.json", "w+") as f:
        f.write(jsonStr)


# ----------------------------------------------------------------------------------------------


num = int(len(allLinks))
grupedLinks = []

nGroups = 26
o = range(0, num, nGroups)
for i in o:
    grupedLinks.append(allLinks[i : i + nGroups])

i = 1
threads = []
for links in grupedLinks:
    x = threading.Thread(
        target=threadFunc,
        args=(
            links,
            proxy,
            i,
        ),
    )
    threads.append(x)
    x.start()
    i = i + 1

for thread in threads:
    thread.join()
