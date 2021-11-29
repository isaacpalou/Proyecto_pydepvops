from typing import Collection
from pymongo import MongoClient


uri = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.qvf0j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(uri)
