import json
import csv

def find_totals(json_string: str, file_name: str) -> None:
  
  data = json.loads(json_string)
  res = [['customer_id','customer_name','total_spent']]

  for customer in data:
      id = customer['customer_id']
      name = customer['customer_name']
      total_sold = 0
      for order in customer['orders']:
          total_sold += (order['quantity']*order['price'])

      res.append([id,name,total_sold])


  with open(file_name, 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerows(res)


json_data = """
  [
    {
      "customer_id": "C001",
      "customer_name": "Alice",
      "orders": [
        {"product_id": "P100", "product_name": "Widget", "quantity": 2, "price": 10.0},
        {"product_id": "P101", "product_name": "Gadget", "quantity": 1, "price": 15.5}
      ]
    },
    {
      "customer_id": "C002",
      "customer_name": "Bob",
      "orders": [
        {"product_id": "P100", "product_name": "Widget", "quantity": 1, "price": 10.0},
        {"product_id": "P102", "product_name": "Thingamajig", "quantity": 3, "price": 7.0}
      ]
    }
  ]
  """

find_totals(json_data,'customer_totals_2.csv')