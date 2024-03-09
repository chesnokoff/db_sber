import pymongo
import time

client = pymongo.MongoClient(host="localhost", port=27017, username='devroot',
                             password='devroot')

db = client.news
collection = db.news
start = time.time()
total_number = collection.count_documents({'title': {'$regex': '.*Russia.*'},
                                           "label": 1})
print("TIME TO SEARCH WITHOUT INDEX: {}".format(time.time() - start))

collection.create_index({'label': 1})

start = time.time()
total_number = collection.count_documents({'title': {'$regex': '.*Russia.*'},
                                           "label": 1})
print("TIME TO SEARCH WITH INDEX: {}".format(time.time() - start))

