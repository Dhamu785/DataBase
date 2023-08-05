import pymongo
import datetime as datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['Krish_tutorial_2']
documents = db['student_info']

# records = [ 
#     {"user":"Krish", "subject":"Database", "score":80}, 
#     {"user":"Amit",  "subject":"JavaScript", "score":90}, 
#     {"user":"Amit",  "title":"Database", "score":85}, 
#     {"user":"Krish",  "title":"JavaScript", "score":75}, 
#     {"user":"Amit",  "title":"Data Science", "score":60},
#     {"user":"Krish",  "title":"Data Science", "score":95}] 

# documents.insert_many(records)

# agg_result= documents.aggregate( 
#     [{ 
#     "$group" :  
#         {"_id" : "$user",  
#          "Total Subject" : {"$sum" : 1} 
#          }} 
#     ]) 
# agg_total= documents.aggregate( 
#     [{ 
#     "$group" :  
#         {"_id" : "$user",  
#          "Total Subject" : {"$sum" : "$score"} 
#          }} 
#     ]) 
# agg_avg= documents.aggregate( 
#     [{ 
#     "$group" :  
#         {"_id" : "$user",  
#          "Total Subject" : {"$avg" : "$score"} 
#          }} 
#     ]) 
# for i in agg_avg:
#     print(i)

# --------------------------------------------------------------------------------------------
# data=[{ "_id" : 1, "item" : "abc", "price" : 10, "quantity" : 2, "date" : datetime.datetime.utcnow()},
# { "_id" : 2, "item" : "jkl", "price" : 20, "quantity" : 1, "date" : datetime.datetime.utcnow() },
# { "_id" : 3, "item" : "xyz", "price" : 5, "quantity" : 5, "date" : datetime.datetime.utcnow() },
# { "_id" : 4, "item" : "abc", "price" : 10, "quantity" : 10, "date" : datetime.datetime.utcnow() },
# { "_id" : 5, "item" : "xyz", "price" : 5, "quantity" : 10, "date" :datetime.datetime.utcnow() }]
# doc = db['store']
# doc.insert_many(data)

### Calculating the average quantity And Average Price
# agg_result=doc.aggregate([
#    {
#       "$group": {
#          "_id": '$item',
#          "avgAmount": {"$avg": {"$multiply": [ "$price", "$quantity" ]}},
#           "avgQuantity": { "$avg": "$quantity" }
#       }
#    }
# ])
# for i in agg_result: 
#     print(i)
    
# --------------------------------------------------------------------------------------------
#### $Project

data_bk=[{
  "_id" : 3,
  "title": "abc123",
  "isbn": "0001122223334",
  "author": { "last": "zzz", "first": "aaa" },
  "copies": 5
},
{
  "_id" : 4,
  "title": "Baked Goods",
  "isbn": "9999999999999",
  "author": { "last": "xyz", "first": "abc", "middle": "" },
  "copies": 2
}]

doc_bk = db['books']
# doc_bk.insert_many(data_bk)

for row in doc_bk.aggregate([{"$project": {"title":1}}]):
    print(row)