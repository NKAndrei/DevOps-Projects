from flask_restful import Resource
from parse_data import getKeys, getPairs, getValues
from parse_data import parse_string_to_json, parse_dict_to_json, parse_list_to_json



## ---- API classes that return JSON response
class GetAll(Resource):
    def __init__(self,**kwargs):
        self.jsonData = kwargs['jsonData']
    def get(self):
        return self.jsonData

class GetKeys(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['jsonData']
        self.key = kwargs['keys']
    def get(self):
        return parse_list_to_json(getKeys(self.data, self.key), "keys")

class GetValues(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['jsonData']
        self.key = kwargs['keys']
    def get(self):
        return parse_list_to_json(getValues(self.data, self.key), "values")

##TODO ---- need to update this API endpoint to return the necessary data in the correct format
##TODO ---- the above API endpoints return the data as a key with array values
##TODO ---- and the javascript is created to iterate through JSON array
class GetPairs(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['jsonData']
        self.key = kwargs['keys']
    def get(self):
        ##return parse_dict_to_json(getPairs(self.data, self.key))
        return parse_list_to_json(getPairs(self.data, self.key), "pairs")


##TODO ---- need to define the rest of these
class GetDate(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']
    def get(self):
        return ""

class GetExchangeType(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']
    def get(self):
        return ""