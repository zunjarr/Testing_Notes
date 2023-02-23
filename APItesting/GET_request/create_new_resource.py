import jsonpath
import requests
import json

# API URL
url = 'https://reqres.in/api/users'

# Read input file GET request
file = open('C:\\Users\\dorugzu\\PycharmProjects\\pythonProject\\APItesting\\CreateUser.json', 'r')
json_input = file.read()            # Data will store in string format
request_input = json.loads(json_input)
print(request_input)
print(type(request_input))

# Make POST request with Json input body
response = requests.post(url, request_input)
print("Response is", response.content)

print(response.json()['id'])
print(type(response.json()))
print('---------------------------------------')
# Validation of Response code
assert response.status_code == 201

# Fetch Header from response
print(response.headers.get('Content-Length'))

# Parse response to Json format
response_Json = json.loads(response.text)

# Pick id using Json path
id1 = jsonpath.jsonpath(response_Json, 'id')
print(id1[0])
