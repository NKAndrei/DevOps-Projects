import json


##! ---- Helper Functions
def getKeyDepth(jsonStructure, keyDepth):
    if len(keyDepth) == 0:
        return jsonStructure
    if len(keyDepth) != 0:
        return jsonStructure[keyDepth]

def getLists(elements_to_parse):
    listOfElements = []
    for x in elements_to_parse:
        listOfElements.append(x)
    return listOfElements
##! ---- Helper Functions



##! ---- End User Functions
def parse_json_string_to_object(string_to_parse):
    parsed_json = json.loads(string_to_parse)
    return parsed_json

def parse_dict_to_json(dict_to_parse):
    json_struct = json.dumps(dict_to_parse)
    return json_struct

def parse_list_to_json(list_to_parse, key_name_to_add):
    jsonString = "{" + "\"" + key_name_to_add + "\"" + " : "  + str(list_to_parse)  + "}"
    jsonString = jsonString.replace("'", "\"")
    return jsonString

def getKeys(jsonStructure, keyDepth):
    keyNames = getKeyDepth(jsonStructure, keyDepth)
    return getLists(keyNames.keys())

def getValues(jsonStructure, keyDepth):
    keyNames = getKeyDepth(jsonStructure, keyDepth)
    return getLists(keyNames.values())
     
def getPairs(jsonStructure, keyDepth):
    keyNames = getKeyDepth(jsonStructure, keyDepth)
    newDict = dict(keyNames.items())
    return newDict
##! ---- End User Functions



##TODO ---- need to define the rest of these ---- more specific functions
def getDates(jsonStructure):
    return ""
def getExchangeType(jsonStructure):
    return ""
def getDataByKey(jsonStructure, key):
    return ""