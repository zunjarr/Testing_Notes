# import pandas as pd
# import wrangler
import re
# fetch_user_data
import pickle

import jsonpath
import requests
import json

# API URL
url = 'https://reqres.in/api/users?page=2'

# Send GET request
response = requests.get(url)

print("response code is ", response)
print("json dumps is ", json.dumps(response.json(), indent=4))
print("Content or Body is ", response.content)
print("Headers are ", response.headers)

assert response.status_code == 200, "Wrong status_code"

# Parsing response to JSON format
json_response = json.loads(response.text)
print("Parsed response to JSON format is ", json_response)

# Fetch value using JSON path
pages = jsonpath.jsonpath(json_response, "total_pages")
print("pages is ", pages)

assert pages[0] == 2, "Wrong total_pages data"
# --------------------------------------------------------------------

# Delete_user
import requests

# API URL
url = 'https://reqres.in/api/users/2'

response = requests.delete(url)

# Fetch response code
print("response is ", response.status_code)

assert response.status_code == 204, "Resource is not deleted"
# --------------------------------------------------------------------

# create_new_resource

# import jsonpath
# import requests
# import json

# API URL
url = 'https://reqres.in/api/users'

# Read input file GET request
file = open('C:\\Users\\dorugzu\\PycharmProjects\\pythonProject\\APItesting\\CreateUser.json', 'r')
json_input = file.read()  # Data will store in string format
request_input = json.loads(json_input)
print(request_input)

# Make POST request with Json input body
response = requests.post(url, request_input)
print("Response is", response.content)

# Validation of Response code
assert response.status_code == 201

# Fetch Header from response
print(response.headers.get('Content-Length'))

# Parse response to Json format
response_Json = json.loads(response.text)

# Pick id using Json path
id1 = jsonpath.jsonpath(response_Json, 'id')
print(id1[0])
# --------------------------------------------------------------------

# add_query_parameters

# import requests

# API URL
base_url = 'https://reqres.in/'  # Domain

# Adding Query parameters to requests
params = {'page': 7}
#                                Path parameter ? Query parameter
# response = requests.get(base_url + "/api/users?page=2")
response = requests.get(base_url + "/api/users", params=params)

print("response code is ", response)
# print("response is ", json.dumps(response.json(), indent=4))
# --------------------------------------------------------------------

# post_request

# import requests
# import json

# POST Request
base_url = 'https://reqres.in/'
payload = {
    "name": "morpheus",
    "job": "leader"
}
response = requests.post(base_url + "/api/users", data=payload)
# print(response.json())
# --------------------------------------------------------------------

# Python_Basic_Que

newlist = [1, 2, 3, 4, 5]
print('Original list is: ', newlist)
newlist.pop()
print('Original list after pop is: ', newlist)  # [1, 2, 3, 4]

numbr = '7 zunjarr 23.56 rugadde 77 gmail. com'
digit = re.findall('\d*\.?\d+', numbr)
print('\ndigit are :', digit)                   # ['7', '23.56', '77']

numbr = '7 zunjarr 23.56 rugadde 77 gmail. com'
digit2 = re.findall('\d+', numbr)
print('\ndigit are :', digit2)                  # ['7', '23', '56', '77']
# ----------------------------------------------------

# Fibonacci Sequence
print('Fibonacci series')
a, b = 0, 1
for i in range(0, 10):
    print(a)
    a, b = b, a + b
# ----------------------------------------------------
# Removing duplicate characters in a string
print('Removing duplicate characters in a string-------------')
# data = input("Enter a string")
data = "PANAMANIAN"
output = ""  # Method 1
for ch in data:
    if ch not in output:
        output = output + ch

print(output)

list1 = []  # Method 2
for ch in data:
    if ch not in list1:
        list1.append(ch)

print(list1)
output2 = ''.join(list1)

print("Original string is: ", data)
print("Result after removing duplicate is: ", output)
print("Result after removing duplicate2 is: ", output2)
# ----------------------------------------------------
# Remove duplicate numbers
dupnum = [10, 10, 30, 20, 40, 70, 70, 50, 50, 40]


def remove_dupli(duplist):
    noduplinum = []

    for ele in duplist:
        if ele not in noduplinum:
            noduplinum.append(ele)

    return noduplinum


print(remove_dupli(dupnum))
# ----------------------------------------------------
# Reverse string

strng = "Mera bharat mahan"
s2 = strng[::-1]  # naham tarahb areM
print(s2)
# ----------------------------------------------------
# To reverse words in a given string

string = "reverse this given string"

s = string.split()[::-1]
print("First reverse is: ", s)  # ['string', 'given', 'this', 'reverse']
new_str = []
for i in s:
    new_str.append(i)
    print(new_str)

print(" ".join(new_str))       # Output: string given this reverse
# ----------------------------------------------------

# Function for reverse string
def my_function(z):
    return z[::-1]

mytxt = my_function("Believe in yourself")
print('Reverse string using Function: ', mytxt)
# Output: flesruoy ni eveileB
# -----------------------------------------------------------------

# Remove consecutive duplicate characters
givenstr = "AAABBBCCCCDDDDDE"
s = ''
for char in givenstr:
    if s == '' or char != s[len(s) - 1]:
        s = s + char
print('Removed consecutive duplicate characters: ', s)
# Output: ABCD
# -----------------------------------------------------
# iterator- It will give one value at a time
nums = [1, 3, 5, 6, 16]

it = iter(nums)

print(next(it))
print(next(it))
print(next(it))

# ----------------------------Till-29-May------------------------------------

exampleJSON = '{"test1":[{"lang1": "Java", "lang2": "Python", "other":["fortran", "Zunjarr", "C"]}]}'
print(type(exampleJSON))
data = json.loads(exampleJSON)
print(type(data))
print(data["test1"][0]["other"][1])

# ----------------------------Started from -6-July------------------------------------
print("Study started")

a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)

# ----------------------------------------------------
for letter in 'Zunjarr':
    print(letter)

for word in ('My', 'name', 'is', 'Zunjarr'):
    print(word)

for byte in b'ABCD':
    print(byte)
# ----------------------------------------------------

new_list = ["12", "15", "5", "14", "6", "3", "1"]
print("Original new_list", new_list)

new_list_sorted = sorted(new_list, key=str)
print("Using sorted method ", new_list_sorted)

# a = new_list.sort()     # Function 'sort' doesn't return anything : None
# print(a)

print('By sort method', new_list.sort())  # Check this again

new_list.sort(key=str)
print(new_list)
# ----------------------------------------------------
# Bubble sort
print('Bubble sort is :')
data_list = [-7, -16, 5, 23, 0, -5, 37, 34]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for i in data_list:
        if i < minimum:
            minimum = i
    new_list.append(minimum)
    data_list.remove(minimum)

print('new_list is ', new_list)

# ----------------------------------------------------
# prod_df = wr.s3.read_parquet(path=prod_s3_parquet_location, dataset=True)
# prod_df.head()
#
# prod_df.to_csv(f'C:/Users/patilan/Desktop/filesize_paratek/{customer_name}/{table_name}/prod.csv', index=False)
# ----------------------------------------------------
# ZIP function

student = ['Ram', 'Sham', 'Raj', 'Jay', 'Viru']
Marks = [10, 20, 30, 40, 50]
Subject = ['Maths', 'Science', 'History', 'Marathi', 'Hindi']

for stud, mark, sub in zip(student, Marks, Subject):
    print(f'{stud} has {mark} marks in {sub}')
# Ram has 10 marks in Maths
# Sham has 20 marks in Science
# Raj has 30 marks in History
# Jay has 40 marks in Marathi
# Viru has 50 marks in Hindi

student = ['Ram', 'Sham', 'Raj', 'Jay', 'Viru']
Marks = [10, 20, 30, 40, 50]
Subject = ['Maths', 'Science', 'History', 'Marathi', 'Hindi']

for value in zip(student, Marks, Subject):
    print('Zip function tuple: ', value)
# Zip function tuple:  ('Ram', 10, 'Maths')
# Zip function tuple:  ('Sham', 20, 'Science')
# Zip function tuple:  ('Raj', 30, 'History')
# Zip function tuple:  ('Jay', 40, 'Marathi')
# Zip function tuple:  ('Viru', 50, 'Hindi')
# ----------------------------------------------------
student1 = ['Ram', 'Sham', 'Raj']
Marks1 = [10, 20, 30]
student1.extend(Marks1)
print(student1)  # ['Ram', 'Sham', 'Raj', 10, 20, 30]

student1.append(Marks1)
print(student1)  # ['Ram', 'Sham', 'Raj', 10, 20, 30, [10, 20, 30]]
# ----------------------------------------------------
# Pickling and Unpickling
# import pickle
cars = ['BMW', 'Maruti', 'i20', 'Baleno', 'Swift']
file = "mycar.pkl"
fileobj = open(file, "wb")
pickle.dump(cars, fileobj)
fileobj.close()

# Unpickling
file = "mycar.pkl"
fileobj = open(file, "rb")
mycar = pickle.load(fileobj)
# print('mycar is ', mycar)
# print(type(mycar))
# ----------------------------------------------------
# Count of the characters
print('Count of the characters: ')

str2 = input("Enter any string: ")
ch = input("Enter which char count you want: ")
count = 0
for i in str2:
    if i == ch:
        count = count + 1

print(ch, 'occurred', count, 'times')
# ----------------------------------------------------
# Count of the characters using count method
print('Count of the characters by Count method: ')
str_data = input("Enter the string: ")

for char in str_data:
    print(char, 'occurred', str_data.count(char), 'times')


from collections import Counter
str_data2 = "ab 25 cd 7z"
cnt = Counter(str_data2)
print(cnt)
# ----------------------------------------------------
# Count numbers and letters
print('#' * 25)
print('Count numbers and letters : ')
str_data3 = "ab 25 cd 7z"

numbers = 0
letters = 0
num = []
let = []
for x in str_data3:
    if x.isdigit():
        numbers += 1
        num = num.append(x)
        print(num)
    elif x.isalpha():
        letters += 1
        let = let.append(x)
        print(let)

print("Letters count is: ", letters)  # Letters: 4
print("Numbers count is: ", numbers)  # Numbers: 3
# print("Letters are: ",  let)     # Letters: abcd
# print("Numbers are: ", num)      # Numbers: 257

# ----------------------------------------------------
a_string = 'Once upon a time'
print(len(re.findall('e', a_string)))
print(len(re.findall('o', a_string)))
# ----------------------------------------------------
# Prime number
nums = 6

# if num > 1:
for i in range(2, nums//2):
    if (nums % i) == 0:
        print(nums, "is not a prime number")
        break
else:
    print(nums, "is a prime number")
# ----------------------------------------------------

# Monkey Patching
class Test:

    def class_method(self):
        print("This is a class method")

def monkey_function():
    print("This is a Monkey function")


Test.class_method = monkey_function
Test.class_method()
# ----------------------------------------------------

# vowels in string
sentence = input('Enter a string:')
vowels = 'A,a,E,e,I,i,O,o,U,u'
Count = 0
for each_char in sentence:
    if each_char in vowels:
        Count += 1
print('There are {} vowels in the string: \'{}\''.format(Count, sentence))
print(f'There are {Count} vowels in given string {sentence}')
# -----------------------------------------------------------

# Separate 1 and 0

# nums = [1, 0, 1, 0, 1, 0, 1, 0]
# new_num1 = []
# print(type(new_num1))
# new_num0 = []
#
# for i in nums:
#     print(i)
#     if i == 1:
#         new_num1 = new_num1.append(i)
#         print(new_num1)
#     else:
#         new_num0 = new_num0.append(i)
#         print(new_num0)

# print(new_num1)
# print(new_num0)
# ----------------------------------------------------

# Input : aabbbcdddd
# Output : a2b3c1d4

strng = 'aabbbcdddd'
Count2 = 0
emp_char = []
for i in strng:
    if i in emp_char:
        Count2 += 1
# ----------------------------------------------------

# Input : a2b3c1d4
# Output : aabbbcdddd
# ----------------------------------------------------

# Regular Expression
email = '7zunjarr_dorugadde@gmail.com'

pattern = re.compile(r'^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$')
# print('ab\ncd')
# print(r'ab\ncd')

if re.search(pattern, email):
    print('its Valid email')
else:
    print('its not Invalid email')

numbr = '7 zunjarr 23.56 rugadde 77 gmail. com'
digit = re.findall('\d*\.?\d+', numbr)


# matches = pattern.finditer(email)
#
# for match in matches:
#     print(match)
# ----------------------------------------------------

def is_isogram(st):
    st = st.lower()
    # st.is_isogram()
    return len(set(st)) == len(st)


print(is_isogram("Dermatoglyphics"))  # True
print(is_isogram("aba"))  # False
print(is_isogram("moOse"))  # False
print(is_isogram(""))  # True


def is_isogram1(string2):
    string2 = string2.lower()
    for char in string2:
        if string2.count(char) > 1:
            return False
    return True


print(is_isogram1("Dermatoglyphics"))  # True
print(is_isogram1("aba"))  # False
print(is_isogram1("moOse"))  # False
print(is_isogram1(""))  # True
# ----------------------------------------------------

class Employee:
    def __init__(self, name, age, dob):
        self.name = name  # public member
        self._dob = dob  # protected member
        self.__age = age  # private member

    def display(self):
        print(self.name)
        print(self.age)


emp = Employee('Mathew', 25, 1991)
print(emp.name)
print(emp._Employee__age)  # Accessing private data
print(emp._dob)  # Accessing protected data
# ----------------------------------------------------
