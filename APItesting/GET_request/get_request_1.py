import requests
import json

response = requests.get('https://reqres.in/api/users/2')
             # params={'/api/users/2'},)
# print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)
# print(dict_response)
# print(type(dict_response))
# print(dict_response[0])
json_response = response.json()
print(json_response)
print('Type of response is ', type(json_response))
print(json_response['data']['email'])
print(json_response['support']['url'])
for user in json_response:
    print(user)
# json_response = list(json_response)
# print(type(json_response))
# print(json_response)
# print(json_response[0]['data'])   #Throwing error
assert response.status_code == 200
# print(response.headers)
assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Wrong comparision"
# Retrieve User details
list_of_user_response = requests.get('https://reqres.in/api/users?page=2')
print('List of users', list_of_user_response.content)
print('List of users2', list_of_user_response.headers)
# for user in list_of_user_response:
#     print(type(user))

