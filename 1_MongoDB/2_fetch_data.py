import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['Krish_tutorial_2']
documents = db['employe_information']
data = {
    "First name": "Krish0",
    "second name": "naik0",
    "department": "Analytics",
    "qualification": "MBA",
    "age": 30
}
# documents.insert_one(data)

data2 = [
    {
        "First name": "Karthi1",
        "second name": "M",
        "department": "Digital Marketing",
        "qualification": "B.Tech",
        "age": 21
    },
    {
        "First name": "Jagan1",
        "second name": "KSG",
        "department": "Researcher",
        "qualification": "M.Tech",
        "age": 24
    },
    {
        "First name": "Padmanathan1",
        "second name": "K",
        "department": "Analyst",
        "qualification": "Bio-Tech",
        "age": 23
    },
    {
        "First name": "Sreejesh1",
        "second name": "S",
        "department": "Application testing",
        "qualification": "CSE",
        "age": 20
    }
]

# documents.insert_many(data2)

# SIMPLE QUERY
# 1. To retrive single record
# result = documents.find_one()
# print(result)

# 2. To retrive multiple record
# for i in documents.find({}):
#     print(i)
    
# 3. To retrive specific record
# for j in documents.find({"First name": "Karthi1"}):
#     print(j)

# 4. Querying by operators
# for k in documents.find({"qualification":{"$in":["CSE","M.Tech"]}}):
#     print(k)

# 5. Querying by and and less than
# for l in documents.find({"qualification":{"$in":["CSE","M.Tech"]},"age":{"$lt":29}}):
#     print(l)
    
# 6. or operator
# for m in documents.find({"$or":[{"qualification":"CSE"},{"age":{"$lt":29}}]}):
#     print(m)

# 7. and operator
# for m in documents.find({"$and":[{"qualification":"CSE"},{"age":{"$lt":29}}]}):
#     print(m)

# ADD NESTED DOCUMENTS
inventory = db.inventory
# inventory.insert_many( [
#    { 'item': "journal", 'qty': 25, 'size': { 'h': 14, 'w': 21,'uom': "cm" }, 'status': "A" },
#    { 'item': "notebook", 'qty': 50,'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "A" },
#    { 'item': "paper", 'qty': 100, 'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "D" },
#    { 'item': "planner", 'qty': 75, 'size': { 'h': 22.85,'w': 30,'uom': "cm" },'status': "D" },
#    { 'item': "postcard", 'qty': 45, 'size': { 'h': 10, 'w': 15.25,'uom': "cm" },'status': "A" },
#    { 'items': ["a", "b", "c"], 'status': "A" }
# ])

# for i in inventory.find({"size":{"h":14,"w":21,"uom":"cm"}}):
#     print(i)

for i in inventory.find({'items': ["a", "b", "c"]}):
    print(i)
