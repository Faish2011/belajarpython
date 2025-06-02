import requests

import json


api_url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get (api_url)

data = response.json ()

for todo in data:
    if todo ["completed"] == True:

        json_object = json.dumps (todo, indent = 3)
        print (json_object)








































