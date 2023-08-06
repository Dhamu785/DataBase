import pymongo
client = pymongo.MongoClient("mongodb+srv://***:***@online-tutorial-krish.****.mongodb.net/")
db = client['Krish-Tutorial']
documents = db['Student_details']

documents.insert_one({"name":"Krish", "age":20, "city":"Ranchi"})