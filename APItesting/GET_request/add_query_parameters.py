import jsonpath
import requests
import json


# API URL
# URL = 'https://reqres.in/api/users?page=2'
base_url = 'https://reqres.in/'   #Domain/Host

# Adding Query parameters to requests
params = {'page': 7}
                                #Path parameter ? Query parameter
# response = requests.get(base_url + "/api/users?page=2")
response = requests.get(base_url + "/api/users", params=params)

print("response code is ", response)
print("response code is ", response.status_code)
print("response code is ", response.content)
# print("response is ", json.dumps(response.json(), indent=4))
