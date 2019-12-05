from pymongo import MongoClient

##TODO ---- define mongo client address, collection and classes
##TODO ---- CRUD classes, refresh old data, 
mongoClient = MongoClient(port=28000)
statistics_values = mongoClient.statistics_values

##! ---- empty class definitions ---- need to be impemented and tested
class CreateCollection():
    def create(self):
        return ''

class DeleteCollection():
    def delete(self):
        return ''

class UpdateValues():
    def update(self):
        return ''

class DeleteValues():
    def delete(self):
        return ''

class ReadAllValues():
    def get(self):
        return ''

class PutValues():
    def put(self):
        return ''
