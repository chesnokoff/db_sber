import pymongo
import time

client = pymongo.MongoClient(host="localhost", port=27017, username='devroot',
                             password='devroot')

db = client.news
collection = db.news
start = time.time()
for i in range(10000):
    collection.insert_one(
        {"title": "YouTube Combines 360-Degree Videos And Snoop Dogg",
         "author": "Chesnokoff",
         "text": "YouTube has announced a new feature, "
                 "courtesy of content studio Portal A, and the video sharing "
                 "site’s head of comedy Ben Relles. “Today we’re excited to "
                 "announce a feature that people have been asking about since "
                 "we launched,” says Relles, who plays the company’s director "
                 "of innovation in an announcement video. “The ability to "
                 "watch every video in 360 — with Snoop Dogg.”",
         "label": 1})
print("TIME: {}".format(time.time() - start))
