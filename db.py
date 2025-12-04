from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["fitcluster"]
usuarios_collection = db["usuarios"]