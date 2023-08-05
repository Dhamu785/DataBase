import pymongo 

# Establish the connection
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create the database
mydb = client["Krish_tutorial_2"]

# Create the connections and insert single data
data = mydb.employe_information
# record = {"First name": "Krish1",
#           "second name": "naik1",
#           "department": "Analytics"}

# data.insert_one(record)

# Insert multiple data
record = [{"First name": "Krish0",
          "second name": "naik0",
          "department": "Analytics"},
          {"First name": "Krish1",
          "second name": "naik1",
          "department": "Analytics"},
          {"First name": "Krish2",
          "second name": "naik2",
          "department": "Analytics"}]

data.insert_many(record)