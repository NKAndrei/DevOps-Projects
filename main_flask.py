from flask import Flask, render_template, request
from flask_restful import Resource, Api
from resources import GetAll, GetKeys, GetPairs, GetValues, GetNewData



app = Flask(__name__)
api = Api(app)
##web_page_url = 'https://api.exchangeratesapi.io/latest'
key = 'rates'




@app.route('/home')
def home():
    #return render_template('home.html', name=parsed_json['rates'])
    return render_template('presentation.html')



## ---- create API endpoints from the rates of the extracted json object
api.add_resource(GetNewData, '/newData', methods=['PUT', 'POST', 'GET'])
api.add_resource(GetAll, '/all', resource_class_kwargs={'jsonData' : "temp", 'keys': key})
api.add_resource(GetKeys, '/allKeys', resource_class_kwargs={'jsonData' : "temp", 'keys': key})
api.add_resource(GetValues, '/allValues', resource_class_kwargs={'jsonData' : "temp", 'keys': key})
api.add_resource(GetPairs, '/allPairs', resource_class_kwargs={'jsonData' : "temp", 'keys': key})



if __name__ == '__main__':
    app.run(debug=True)