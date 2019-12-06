from pymongo import MongoClient

#mongoClient = MongoClient("mongodb://127.0.0.1:27017/")
#pythonStatisticsDB = mongoClient["python_statistics"]
#statisticsCollection = pythonStatisticsDB["statistics_values"]



##TODO ---- need to add error handling
##TODO ---- needs further testing ---- works from innitial tests
## ---- used to establish innitial connection to a db
## ---- can return db, collection, new connections
class DBConnection():
    def __init__(self, mongoEndpoint, dbName, collectionName):
        self.dbName = dbName
        self.collectionName = collectionName
        self.mongoClient = MongoClient(mongoEndpoint)
    def getClient(self):
        return self.mongoClient
    def getDB(self):
        pythonMongoDB = self.mongoClient[self.dbName]
        return pythonMongoDB
    def getConnection(self):
        pythonMongoDB = self.mongoClient[self.dbName]
        pythonMongoCollection = pythonMongoDB[self.collectionName]
        return pythonMongoCollection
    def getNewConnection(self, newCollectionName):
        pythonMongoDB = self.mongoClient[self.dbName]
        pythonMongoCollection = pythonMongoDB[newCollectionName]
        return pythonMongoCollection

## ---- used to do CRUD operations on a given collection in a mongo db
## ---- requires a connection object and all passed arguments must be a Python Object type
class DBOperations():
    def __init__(self, dbConnection):
        self.dbConnection = dbConnection
    def getOne(self, filterBy, fieldsToReturn): ##! ---- gets the first inserted document or the first occuring ---- requires dicts
        result = self.dbConnection.getConnection().find_one(filterBy, fieldsToReturn)
        return result
    def getAll(self, filterBy, fieldsToReturn):
        result = self.dbConnection.getConnection().find(filterBy, fieldsToReturn)
        return result
    def putOne(self, objectToInsert):
        insertId = self.dbConnection.getConnection().insert_one(objectToInsert).inserted_id
        return { 'id' : insertId }
    def putAll(self):
        return ''
    def removeOne(self, objectToDelete): ##! ---- deletes only the first document
        removedItem = self.dbConnection.getConnection().delete_one(objectToDelete)
        return removedItem
    def removeAll(self, objectToDelete):
        removedItems = self.dbConnection.getConnection().delete_many(objectToDelete)
        return removedItems



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
