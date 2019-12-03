from flask import Flask, render_template
from flask_restful import Resource, Api
from resources import GetAll, GetKeys, GetPairs, GetValues
import web_requests
from parse_data import getKeys, getPairs, getValues, parse_string_to_json, parse_dict_to_json, parse_list_to_json

app = Flask(__name__)
api = Api(app)


## ---- download the json response from the given URL and parse it as a json object
## ---- use key of json value "rates"
web_page_url = 'https://api.exchangeratesapi.io/latest'
data_to_parse = web_requests.getPageData(web_page_url).decode()
parsed_json = parse_string_to_json(data_to_parse)
key = "rates"


## ---- create API endpoints from the rates of the extracted json object
api.add_resource(GetAll, '/all', resource_class_kwargs={'jsonData' : parsed_json, 'keys': key})
api.add_resource(GetKeys, '/allKeys', resource_class_kwargs={'jsonData' : parsed_json, 'keys': key})
api.add_resource(GetValues, '/allValues', resource_class_kwargs={'jsonData' : parsed_json, 'keys': key})
api.add_resource(GetPairs, '/allPairs', resource_class_kwargs={'jsonData' : parsed_json, 'keys': key})

@app.route('/home')
def home():
    #return render_template('home.html', name=parsed_json['rates'])
    return render_template('presentation.html')



if __name__ == '__main__':
    app.run(debug=True)