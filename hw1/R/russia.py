import pymongo

client = pymongo.MongoClient(host="localhost", port=27017, username='devroot',
                             password='devroot')

db = client.news
collection = db.news
fake_number = collection.count_documents({'title': {'$regex': '.*Russia.*'},
                                          "label": 1})
true_number = collection.count_documents({'title': {'$regex': '.*Russia.*'},
                                          "label": 0})
total_number = collection.count_documents({'title': {'$regex': '.*Russia.*'}})
print("Всего {} новостей о России, из них {} ложные и {} достоверные".format(
    total_number, fake_number, true_number))
results = collection.find({'title': {'$regex': '.*Russia.* war.*'}}).limit(3)
for result in results:
    print(result)
