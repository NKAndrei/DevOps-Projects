from mongoDB import DBConnection, DBOperations
import json


## ---- create a db connection and read data from a file
connection = DBConnection('mongodb://127.0.0.1:27017/', 'python_statistics', 'statistics_values')
operations = DBOperations(connection)
file = open("temp", "r")
data = file.read()
file.close()



## ---- insert data into db, retrieve it and delete it
operations.putOne(json.loads(data))
print(str(operations.putOne(json.loads("{ \"id\" : 7}"))))
print("objects inserted")
print(operations.getOne(json.loads("{ \"id\" : 7}"), json.loads("{ \"id\" : 1 }")))
for x in operations.getAll(json.loads("{}"), json.loads("{}")):
    print(x)
print(operations.removeAll(json.loads("{}")).deleted_count)