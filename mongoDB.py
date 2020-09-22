from pymongo import MongoClient

#mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
#pythonStatisticsDB = mongo_client["python_statistics"]
#statisticsCollection = pythonStatisticsDB["statistics_values"]



##TODO ---- need to add error handling
##TODO ---- needs further testing ---- works from innitial tests
## ---- used to establish innitial connection to a db
## ---- can return db, collection, new connections
class DBConnection():
    def __init__(self, mongo_endpoint, db_name, collection_name):
        self.db_name         = db_name
        self.collection_name = collection_name
        self.mongo_client    = MongoClient(mongo_endpoint)
    
    def get_client(self):
        return self.mongo_client
    
    def get_db(self):
        python_mongodb = self.mongo_client[self.db_name]
        return python_mongodb
    
    def get_connection(self):
        python_mongodb          = self.mongo_client[self.db_name]
        python_mongo_collection = python_mongodb[self.collection_name]
        return python_mongo_collection
    
    def get_new_connection(self, newCollectionName):
        python_mongodb          = self.mongo_client[self.db_name]
        python_mongo_collection = python_mongodb[newCollectionName]
        return python_mongo_collection

## ---- used to do CRUD operations on a given collection in a mongo db
## ---- requires a connection object and all passed arguments must be a Python Object type
class DBOperations():
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def get_one(self, filter_by_string, fields_to_return): ##! ---- gets the first inserted document or the first occuring ---- requires dicts
        result = self.db_connection.get_connection().find_one(filter_by_string, fields_to_return)
        return result
    
    def get_all(self, filter_by_string, fields_to_return):
        result = self.db_connection.get_connection().find(filter_by_string, fields_to_return)
        return result
    
    def put_one(self, object_to_insert):
        insertid = self.db_connection.get_connection().insert_one(object_to_insert).inserted_id
        return { 'id' : insertid }
    
    def put_all(self):
        return ''
    
    def remove_one(self, object_to_delete): ##! ---- deletes only the first document
        removed_item = self.db_connection.get_connection().delete_one(object_to_delete)
        return removed_item
    
    def remove_all(self, object_to_delete):
        removed_items = self.db_connection.get_connection().delete_many(object_to_delete)
        return removed_items



##! ---- empty class definitions ---- need to be impemented and tested
class CreateDB():
    def create(self):
        return ''

class DeleteDB():
    def delete(self):
        return ''

class CreateCollection():
    def create(self):
        return ''

class DeleteCollection():
    def delete(self):
        return ''
