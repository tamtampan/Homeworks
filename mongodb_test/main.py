from pymongo import MongoClient

# connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# select the database and collection to work with
db = client["test"]
collection = db["test3"]

# insert a document into the collection
document = {"name": "John", "age": 30}
result = collection.insert_one(document)
print("Inserted document with ID:", result.inserted_id)

# retrieve all documents from the collection
documents = collection.find()
for document in documents:
    print(document)

# from mongoengine import *
