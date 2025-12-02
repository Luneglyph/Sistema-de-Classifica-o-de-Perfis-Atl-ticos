# db.py
# conecta no mongodb e define a collection de usuarios

from pymongo import MongoClient

# conecta no mongodb local
client = MongoClient("mongodb://localhost:27017/")

# define o banco e a collection
db = client["fitcluster"]
usuarios_collection = db["usuarios"]