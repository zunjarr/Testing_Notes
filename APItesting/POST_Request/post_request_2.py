import requests
from payloads import *
import configparser
from utilities.configuration import *
from requests.auth import HTTPBasicAuth

# post_request_respo = getConfig(path)
# print(post_request_respo)

# config = getConfig()
# print('getConfig method returns the value is ', config)
post_resp = requests.post(getConfig() + '/api/users', json=add_user_payload(), )
print('post_resp status_code is ', post_resp.status_code)
print('post_resp is ', post_resp)
assert post_resp.status_code == 201, "Resource is not created"

# print(post_resp.json())
# print(type(post_resp.json()))
# respo_json = post_resp.json()
# userId = respo_json['id']
# print("Newly created user id= ", userId)
# print(type(userId))
# userId = int(userId)
# print(type(userId))

# Delete User
# del_url = requests.post('https://reqres.in/api/users/2', json={'id': userId})
# delete_response = requests.delete(del_url)
# print(delete_response.status_code)
# assert delete_response.status_code == 204, "Resource is not deleted"
# del_url = requests.delete('https://reqres.in/api/users/userId')
# delete_response = requests.delete(del_url)
# print(delete_response)
# assert delete_response.status_code == 204, "Resource is not deleted"

# Authentication
# url = 'https://api.github.com/user'
url = 'https://github.com/zunjarr/zunjarr'
github_respo = requests.get(url, auth=('zunjarrdorugadde@gmail.com', 'Chain@zz$1@'))
print('github_respo is ', github_respo)
# assert github_respo == 200, "You require authentication"

# resp_auth = requests.get('https://passwordinator.herokuapp.com/generate')
# print(resp_auth.content)

# Basic authentication
api_token = 'CdTKOsLpiFNdDjWFPEc7E19D'
respo_atlass = requests.get(getAuthUrl(), auth=('codewithderrick@gmail.com', api_token))
print('respo_atlass is ', respo_atlass)

# Postman Basic authentication (base64encode.org)
url_postman = 'https://postman-echo.com/basic-auth'
respo_postman = requests.get(url_postman, auth=('postman', 'password'))
print('respo_postman is ', respo_postman)

# Session management
se = requests.session()
se.auth = auth=('postman', 'password')
url_postman2 = 'https://postman-echo.com/basic-auth'
respo_postman_se = se.get(url_postman2)
print('respo_postman2 is ', respo_postman_se)

# Cookie management
se = requests.session()
se.cookies.update({'visit-month': 'April'})     # Common cookie

respo_cooki = requests.get('http://httpbin.org/cookies', cookies={'visit-year': '2022'})
respo_cooki_se = se.get('http://httpbin.org/cookies', cookies={'visit-year': '2022'})
print('respo_cooki is ', respo_cooki_se.text)

# Redirection and Timeout
cookie = {'visit-month': 'February'}
respo_cooki_redir = requests.get('http://httpbin.org/', cookies=cookie, allow_redirects=False, timeout=1)
#301, 200
print('respo_cooki_redir history is ', respo_cooki_redir.history)
print('respo_cooki_redir status_code is ', respo_cooki_redir.status_code)
