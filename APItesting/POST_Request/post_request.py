import json
import requests

# POST Request
base_url = 'https://reqres.in/'
payload = {
    "name": "morpheus",
    "job": "leader"
}
response_post = requests.post(base_url + "/api/users", data=payload)
print('post response is ', response_post)
# print(response.json())

# PUT Request
payload_put = {
    "name": "morpheus",
    "job": "zion resident"
}
response_put = requests.put(base_url + "/api/users/22", data=payload_put)
print('put response is ', response_put)
# print(response2.json())

# Delete Request
url = 'https://reqres.in/api/users/2'
response_del_1st = requests.delete(url)
# OR
response_del_2nd = requests.put(base_url + "/api/users/2")
print('delete response is ', response_del_1st.status_code)

assert response_del_1st.status_code == 204, "Resource is not deleted"

# ------------------------------------------------------------------------------------
json1 = '{"Company": "Jio", "Sim": "Dual"}'

dict1 = json.loads(json1)  # json.loads converts 'json string' into 'Dict'
print(dict1)
print(type(dict1))
print(dict1.get('Sim'))

dict2 = {"Company": "Jio", "Sim": "Dual"}

json2 = json.dumps(dict2, indent=4)  # json.dumps converts 'Dict' into 'json string'
print(json2)
print(type(json2))
# print(json2.get('Company'))             # AttributeError: 'str' object has no attribute 'get'


dict1 = json.load(json1)        # The json. load() is used to read the JSON document from file
                                # The json. loads() is used to convert JSON String document into Python dictionary

# ------------------------------------------------------------------------------------
# Programming Hero Auther
# import pywhatkit
# from flask import Flask, request
# pywhatkit.sendwhatmsg('+918698165771', 'Message sent by automated script', 23, 15)
# pywhatkit.sendwhatmsg('+919637526388', 'Message sent by automated script', 23, 8)
# ------------------------------------------------------------------------------------

# class Scaler:
#     Course1 = 'Python'
#     Course2 = 'C++'
#     Course3 = 'Java'
# # Accessing the values of the attributes
# print(Scaler.Course1)
# print(Scaler.Course3)
# # Accessing through object instantiation.
# obj= Scaler()
# print(obj.Course2)
# ------------------------------------------------------------------------------------
