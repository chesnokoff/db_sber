import pymongo

client = pymongo.MongoClient(host="localhost", port=27017, username='devroot',
                             password='devroot')

db = client.news
collection = db.news

collection.insert_many(
    [{"id": "test",
      "title": "Replace",
      "author": "Chesnokoff",
      "text": "Test",
      "label": 1},
     {"id": "test",
      "title": "Update",
      "author": "Chesnokoff",
      "text": "Test",
      "label": 1}]
)

collection.find_one_and_replace({"title": "Replace"}, {"id": "test",
                                                       "organization": "MIPT",
                                                       "title": "Replace",
                                                       "text": "Test",
                                                       "label": 1})
collection.find_one_and_update({"title": "Update"},
                               {'$set': {"organization": "MIPT"},
                                "$unset": {"author": ""}})
