import requests
import json
import jsonpath

# API URL
url = 'https://reqres.in/api/users'

# GET request
response = requests.get(url)

print("response code is ", response)
print("response code or status_code is ", response.status_code)
print("Content or Body is ", response.content)
# print(type(response.content))
print("Headers are ", response.headers)
# print(type(response.headers))

assert response.status_code == 200, "Wrong status_code"

# Parsing response to JSON format
json_response = json.loads(response.text)
print("Parsed response to JSON format is ", json_response)
print(type(json_response))

print("json dumps is ", json.dumps(response.json(), indent=4))
dumps_data = json.dumps(response.json(), indent=4)
print(type(dumps_data))                     # <class 'str'>

print("response.json is ", response.json())
print(type(response.json()))                # <class 'dict'>

# Fetch value using JSON path
pages = jsonpath.jsonpath(json_response, "total_pages")
print(type(pages))                          # <class 'list'>
print("Fetched pages value is ", pages)

assert pages[0] == 2, "Wrong data of total_pages "
