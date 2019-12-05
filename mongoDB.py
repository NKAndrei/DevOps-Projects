from pymongo import MongoClient

mongoClient = MongoClient(port=28000)
statistics_values = mongoClient.statistics_values