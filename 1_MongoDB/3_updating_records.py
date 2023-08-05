import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['Krish_tutorial_2']
documents = db['employe_information']

# documents.update_one({"item": "paper"},
#                      {'$set': {"size.uom": "M", "status": "P"},
#                       '$currentDate': {"lastModified": True}})

# documents.update_many({"qty": {"$lt": 50}},
#                      {'$set': {"size.uom": "CC", "status": "CC"},
#                       '$currentDate': {"lastModified": True}})

documents.replace_one({"item": "paper"},
                      {"title":"Replace one",
                       "Inventory":{"a":50, 
                                    "b":20}})


# MY PRACTICE
# for i in documents.find({"Inventory.a": 50}):
#     print(i)
