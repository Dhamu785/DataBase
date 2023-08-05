# **MongoDB** 
## **MongoDB installation and Mangosh PowerShell**

### Overview
- Stores data in the format of json, key-value pairs.
- Fast retrieval of data.
 
### Download and setups
* Download the MongoDB compass from [here](https://www.mongodb.com/try/download/community).
* Download the MongoDB shell from [here](https://www.mongodb.com/try/download/shell).
	* Set the bin location in the system variable path.

### Create database and collections in mongosh
- Open the command prompt and run 
```cmd
mongosh
```
* To_Create_database 
```cmd
use database_name
```
* create_collections_and_add_one_record 
```cmd
db.collection_name.insertOne({"First name":"Dhamu", "last name": "R"})
```
* Create_collections_and_add_multiple_records 
```cmd
db.collection_name.insertMany([{"first name" : "Krish1", "last name":"Naik1"},{"first name":"Krish2","last name":"Naik2"}])
```
* Query_all_data 
```cmd
db.collection_name.find()
```
* Fetch_particular_data 
```cmd
db.collection_name.find({"first name":"Krish"})
```
---

## **MongoDB with python**

- **To install the python library** run the below script in the cmd prompt
	```python
	pip install pymongo
	```
- Refer the [script](https://github.com/Dhamu785/DataBase/blob/main/1_MongoDB/1_Basic_connections.py) for 
	- establishing connection 
	- create database
	- insert single data
	- insert multiple data
- Refer this [script](https://github.com/Dhamu785/DataBase/blob/main/1_MongoDB/2_fetch_data.py) for 
	- Querying data
	- Nested documents
- Refer the [script](https://github.com/Dhamu785/DataBase/blob/main/1_MongoDB/3_updating_records.py) for the following functions
	- update_one()
	- update_many()
	- replace_one()
- Refer the [script](https://github.com/Dhamu785/DataBase/blob/main/1_MongoDB/4_Aggregate%20Functions.py) for 
	- sum
	- average
	- multiply
	- project
