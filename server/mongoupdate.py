from pymongo import MongoClient
import json

client = MongoClient(
    'mongodb+srv://Comparazon:sharayu2000@cluster0.vkvevwe.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database('shaurya-test')
records = db.products

with open('/home/shaun/Desktop/Ecommerce-Scraper/final-flipkart-amazon-data.json', 'r') as json_file:
    data = json.loads(json_file.read())

print(len(data))
if (len(data) >= 230):
    if isinstance(data, list):
        records.delete_many({})
        records.insert_many(data)
    else:
        records.delete_many({})
        records.insert_one(data)
