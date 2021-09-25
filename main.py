from fastapi import FastAPI



import json
import csv
import os

# LOAD DATA

products = {}

for filename in os.listdir('data/products/products/en')[:10]:
    with open('data/products/products/en/'+filename, encoding='utf-8') as f:
        data = json.loads(f.read())
        products[data['id']] = data

print('PRODUCT DATA LOADED')

shopping_data = {

}

for filename in os.listdir('data/ShoppingCart')[:1]:
    f = open('data/ShoppingCart/'+filename)
    r = csv.reader(f, delimiter=',')
    for i, row in enumerate(r):
        if i == 0:
            continue

        customer_id = int(row[1])
        if customer_id not in shopping_data:
            shopping_data[customer_id] = []
        shopping_data[customer_id].append({
            "YYYYMM": int(row[0]),
            "KundeID": int(row[1]),
            "WarenkorbID": int(row[2]),
            "ProfitKSTID": int(row[3]),
            "ProfitKSTNameD": row[4],
            "GenossenschaftCode": row[5],
            "TransaktionDatumID": row[6],
            "TransaktionZeit": row[7],
            "ArtikelID": int(row[8]),
            "Menge": float(row[9]),
        })
    f.close()

# FASTAPI APP

app = FastAPI()

@app.get("/data/customer/{customer_id}")
def get_user_stats(customer_id):
    return shopping_data.get(int(customer_id))
