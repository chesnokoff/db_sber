import pymongo

client = pymongo.MongoClient(host="localhost", port=27017, username='devroot',
                             password='devroot')

db = client.news
collection = db.news
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

collection.insert_many(
    [{
        "title": "Hong Kong unveils its second national security law, "
                 "aligning city more closely with mainland China",
        "author": "Chris Lau",
        "text": "Hong Kong’s government unveiled a new suite of powerful "
                "national security laws on Friday that critics and foreign "
                "governments warn could deepen the ongoing crackdown in the "
                "city and further undermine its reputation as an "
                "international "
                "business hub",
        "label": 0},
        {
            "title": "Russian hackers breached key Microsoft systems",
            "author": "Sean Lyngaas",
            "text": "Russian state-backed hackers gained access to some of "
                    "Microsoft’s core software systems in a hack first "
                    "disclosed "
                    "in January, the company said Friday, revealing a more "
                    "extensive and serious intrusion into Microsoft’s systems "
                    "than previously known.",
            "label": 0},
        {"title": "Fake",
         "author": "Chesnokoff",
         "text": "Fake",
         "label": 1}]
)
