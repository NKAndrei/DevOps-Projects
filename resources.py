import sys
import web_requests
from __future__ import print_function
from flask import request, Response
from flask_restful import Resource
from parse_data import parse_json_string_to_object, parse_dict_to_json, parse_list_to_json, get_keys, get_pairs, get_values


##TODO ---- currently all API endpoints write and retrieve all necessary information to a temporary file
##TODO ---- set up a db and a connection to put/retrieve data
##TODO ---- need to set up error handling

## ---- API classes that return JSON responses based on key
class GetAll(Resource):
    def __init__(self,**kwargs):
        self.data = kwargs['jsonData']
    def get(self):
        f         = open(self.data, "r")
        file_data = parse_json_string_to_object(f.read()) 
        f.close()
        return file_data

class GetKeys(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['jsonData']
        self.key  = kwargs['keys']
    def get(self):
        f         = open(self.data, "r")
        file_data = parse_json_string_to_object(f.read()) 
        f.close()
        return parse_list_to_json(get_keys(file_data, self.key), "keys")

class GetValues(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['jsonData']
        self.key  = kwargs['keys']
    def get(self):
        f         = open(self.data, "r")
        file_data = parse_json_string_to_object(f.read()) 
        f.close()
        return parse_list_to_json(get_values(file_data, self.key), "values")

class GetPairs(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['jsonData']
        self.key  = kwargs['keys']
    def get(self):
        f         = open(self.data, "r")
        file_data = parse_json_string_to_object(f.read()) 
        f.close()
        return parse_list_to_json(get_pairs(file_data, self.key), "pairs")

class GetNewData(Resource):
    def post(self):
        self.new_url       = request.get_json(force=True)
        self.data_to_parse = web_requests.get_page_data(self.new_url['url']).decode()
        self.parsed_json   = parse_json_string_to_object(self.data_to_parse)
        
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