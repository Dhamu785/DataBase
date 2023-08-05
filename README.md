> **MongoDB installation and Mangosh PowerShell**

### Overview
- Stores data in the format of json, key-value pairs.
- Fast retrieval of data.
 
### Download and setups
* Download the MongoDB compass from [here](https://www.mongodb.com/try/download/community).
* Download the MongoDB shell from [here](https://www.mongodb.com/try/download/shell).
	* Set the bin location in the system variable path.

### Create database and collections in mongosh
- Open the command prompt and run `mongosh`.
* #Create_database run -> 
	* `use database_name`
	* Now the database is created.
* #create_collections_and_add_one_record run -> 
	* `db.collection_name.insertOne({"First name":"Dhamu", "last name": "R"})`
	* Now the collection is created with the mentioned name and also one record added.
* #create_collections_and_add_multiple_records run ->
	* `db.collection_name.insertMany([{"first name" : "Krish1", "last name":"Naik1"},{"first name":"Krish2","last name":"Naik2"}])`. 
	* Multiple records added to it.
* #Query_all_data run ->
	* `db.collection_name.find()`
	* It will return all the records from the database.
* #Fetch_particular_data run -> 
	* `db.collection_name.find("first name":"Krish")`
	* It will return the data with the first name Krish.


> **MongoDB with python**


