import pymongo
import pandas as pd

client = pymongo.MongoClient(host="localhost", port=27017, username='devroot', password='devroot')
if 'news' in client.list_database_names():
    print('Remove existing database "news"')
    client.drop_database('news')

print('Create database "news"')
db = client.news

print('Create collection "news"')
df = pd.read_csv('data.csv')
db.news.insert_many(df.to_dict('records'))
