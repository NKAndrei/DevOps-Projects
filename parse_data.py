import json


##! ---- Helper Functions
def get_key_depth(json_structure, key_depth):
    if len(key_depth) == 0:
        return json_structure
    if len(key_depth) != 0:
        return json_structure[key_depth]

def get_lists(elements_to_parse):
    list_of_elements = []
    for x in elements_to_parse:
        list_of_elements.append(x)
    return list_of_elements
##! ---- Helper Functions



##! ---- End User Functions
def parse_json_string_to_object(string_to_parse):
    parsed_json = json.loads(string_to_parse)
    return parsed_json

def parse_dict_to_json(dict_to_parse):
    json_struct = json.dumps(dict_to_parse)
    return json_struct

def parse_list_to_json(list_to_parse, key_name_to_add):
    json_string = "{" + "\"" + key_name_to_add + "\"" + " : "  + str(list_to_parse)  + "}"
    json_string = json_string.replace("'", "\"")
    return json_string

def get_keys(json_structure, key_depth):
    key_names = get_key_depth(json_structure, key_depth)
    return get_lists(key_names.keys())

def get_values(json_structure, key_depth):
    key_names = get_key_depth(json_structure, key_depth)
    return get_lists(key_names.values())
     
def get_pairs(json_structure, key_depth):
    key_names = get_key_depth(json_structure, key_depth)
    new_dict  = dict(key_names.items())
    return new_dict
##! ---- End User Functions



##TODO ---- need to define the rest of these ---- more specific functions
def get_dates(json_structure):
    return ""
def get_exchange_type(json_structure):
    return ""
def get_data_by_key(json_structure, key):
    return ""