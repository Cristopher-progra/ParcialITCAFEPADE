import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Parcial1_sis11a-cris"]
collection = db["libro"]



