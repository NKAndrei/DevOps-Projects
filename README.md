# PythonStatisticsPresentation

Small project to create a statistics presenation from information downloaded from an api (used as a college project)

Uses flask, python and mongodb do download json data from an exchange rates broker and create a visual statistics presentation in javascript.

Technologies used:
 - python
 - flask
 - mongodb
 - javascript
 - plotly
 - jinja templates
 
 
Modules and roles:
 - main_flask - the entry point of the application
 - web_requests - used to execute requests to different exchange api
 - resource - contains the api calls used to send, receive and process the data
 - parse_data - a parser used to extract useful information from the exchange api response
 - mongoDB - used to store data of specific graphs and compare them later on
 - db_tests - test the connection and methods on the db
