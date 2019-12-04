from __future__ import print_function
import sys
from flask_restful import Resource
from parse_data import getKeys, getPairs, getValues
from parse_data import parse_string_to_json, parse_dict_to_json, parse_list_to_json
from flask import request, Response
import web_requests

##TODO ---- currently all API endpoints write and retrieve all necessary information to a temporary file
##TODO ---- set up a db and a connection to put/retrieve data
##TODO ---- need to set up error handling

## ---- API classes that return JSON responses based on key
class GetAll(Resource):
    def __init__(self,**kwargs):
        self.data = kwargs['jsonData']
    def get(self):
        f = open(self.data, "r")
        fileData = parse_string_to_json(f.read()) 
        f.close()
        return fileData

class GetKeys(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['jsonData']
        self.key = kwargs['keys']
    def get(self):
        f = open(self.data, "r")
        fileData = parse_string_to_json(f.read()) 
        f.close()
        return parse_list_to_json(getKeys(fileData, self.key), "keys")

class GetValues(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['jsonData']
        self.key = kwargs['keys']
    def get(self):
        f = open(self.data, "r")
        fileData = parse_string_to_json(f.read()) 
        f.close()
        return parse_list_to_json(getValues(fileData, self.key), "values")

class GetPairs(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['jsonData']
        self.key = kwargs['keys']
    def get(self):
        f = open(self.data, "r")
        fileData = parse_string_to_json(f.read()) 
        f.close()
        ##return parse_dict_to_json(getPairs(self.data, self.key))
        return parse_list_to_json(getPairs(fileData, self.key), "pairs")

class GetNewData(Resource):
    def post(self):
        self.newUrl = request.get_json(force=True)
        self.data_to_parse = web_requests.getPageData(self.newUrl['url']).decode()
        self.parsed_json = parse_string_to_json(self.data_to_parse)
        f = open("temp", "w")
        f.write(str(self.data_to_parse))
        f.close()
        return { "status" : 200 }

##TODO ---- need to define the rest of these
class GetDate(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']
    def get(self):
        return ""