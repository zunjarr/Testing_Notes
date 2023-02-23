import re

print([1, 2, 3] * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print((1, 2, 3) * 3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
# print({1, 2, 3} * 3)                  # TypeError: unsupported operand type(s) for *: 'set' and 'int'
# print({1: 'a', 2: 'b', 3: 'c'} * 3)     # TypeError: unsupported operand type(s) for *: 'dict' and 'int'


x = {1, 2, 3, 4, 5}
x.add(5)
x.add(6)
print(x)  # {1, 2, 3, 4, 5, 6}
print('Before comprehension')


var = {x: x * x for x in range(1, 10)}
print(var)


# string1 = [11, 12, 13, 14, 15, 16]
string1 = 'Monty Pythons'
even_list = []
odd_list = []
for i in range(len(string1)):
    if i % 2 == 0:
        even_list.append(string1[i])
    else:
        odd_list.append(string1[i])
print(f"Even characters from string : \n{even_list}")
print(f"\nOdd characters from string : \n{odd_list}")


string = "abcdefghijklmnopqrstuvxyz"
print("\nEven Characters:", string[::2])  # Characters at even index
print("Odd Characters:", string[1::2])  # Characters at odd index


string7 = '38566593'

for num in string7:
    if int(num) % 2 == 1:
        print(num)


string = '38566593'

for i, char in enumerate(string):
    if i % 2 == 1:
        print(f'{i} {char}')


print("1 2 3")

num = 5
# for i in range(2, num):
#     if num % i == 0:
#         print("Not a prime number")
# else:
#     print("Its a prime number")
# ----------------------------------------------------
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
# else:
#     print(num, "is a prime number")
# ----------------------------------------------------

# st = ['ahah']
# st1 = st.is_isogram()
# print(st1)
# ----------------------------------------------------

# s1 = {1, 2, 3, {1, 2, 3}}       # TypeError: unhashable type: 'set'
# print(s1)

s2 = {1, 2, 3, (1, 2, 3)}
print(s2)

# s3 = {1, 2, 3, [1, 2, 3]}       # TypeError: unhashable type: 'list'
# print(s3)
# ----------------------------------------------------

# Count occurrences of each character in string
strx = "i love you too"
res = {}

for i in strx:
    res[i] = res.get(i, 0) + 1

print("Count occurrences of each character in string:" + str(res))
# {'i': 1, ' ': 3, 'l': 1, 'o': 4, 'v': 1, 'e': 1, 'y': 1, 'u': 1, 't': 1}
# ----------------------------------------------------

my_str = 'Bobby'
my_dict = {}

for char in my_str:
    if char.lower() in my_dict:
        my_dict[char.lower()] += 1
    else:
        my_dict[char.lower()] = 1

print(my_dict)  # {'b': 3, 'o': 1, 'y': 1}


# ----------------------------------------------------

def common_char():
    first = input("Enter first string to find common char: ")
    secnd = input("Enter second string to find common char: ")
    first = set(first)
    secnd = set(secnd)
    res = first & secnd
    print(res)


common_char()


# ----------------------------------------------------

def len_last_word(Q):
    arr = Q.split(' ')
    # print(arr)
    size = len(arr)
    # print(size)
    if size == 1:
        print(len(Q))

    last_word = arr[-1]
    print(last_word)
    print(len(last_word))


A = 'My name is Zunjarr'
# A = 'G'
len_last_word(A)
# ----------------------------------------------------

# Take multiple inputs at a time

# a, b, c = map(int, input('Enter 3 strings: ').split())
a, b, c = map(str, input('Enter 3 strings: ').split())
print(a, b, c, end=' ')
# ----------------------------------------------------

strng2 = input('\n Reverse words : ')
li = strng2.split(' ')
for w in li:
    print(w[-1::-1], end=' ')


# print(w[-1])
# ----------------------------------------------------

# Word count
def word_count():
    strng4 = input('\nEnter any string to count words : ')
    lis = strng4.split(' ')
    d = {}

    for i in lis:
        d[i] = d.get(i, 0) + 1

    print(d)


word_count()


# ----------------------------------------------------

# Each char count
def char_count():
    strng4 = input('\nEnter any string to count char : ')
    # lis = strng4.split(' ')
    d = {}

    for i in strng4:
        d[i] = d.get(i, 0) + 1

    print(d)


char_count()
# ----------------------------------------------------
