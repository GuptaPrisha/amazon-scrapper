import json
import os
from pprint import pprint

# with open("./data/data", "r") as f:
#     data = f.read()
#     file = json.loads(data)
#     allLinks = file["data"]
scrapeedProducts = {}
allProducts = []
entries = os.listdir("data")
entries.sort()
for entry in entries:
    with open(f"./data/{entry}", "r") as f:
        data = f.read()
        file = json.loads(data)
        products = file["data"]
        allProducts.extend(products)

scrapeedProducts["data"] = allProducts
jsonStr = json.dumps(scrapeedProducts)

with open("scrapped.json", "w+") as file:
    file.write(jsonStr)
