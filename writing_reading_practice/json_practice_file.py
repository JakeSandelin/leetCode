import json
import csv

with open('writing_reading_practice/json_data.json','r') as f:
    data = json.load(f)


res = [['customer_id','customer_name','total_spent']]

for customer in data:
    id = customer['customer_id']
    name = customer['customer_name']
    total_rev = 0

    for order in customer['orders']:
        total_rev += order['quantity'] * order['price']

    res.append([id,name,total_rev])


with open('writing_reading_practice/json_practice_3.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(res)