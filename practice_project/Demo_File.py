# s1 = {1, 2, 3, {1, 2, 3}}
# print(s1)                     # TypeError: unhashable type: 'set'

# s2 = {1, 2, 3, (1, 2, 3)}
# print(s2)

# s3 = {1, 2, 3, [1, 2, 3]}
# print(s3)                     # TypeError: unhashable type: 'list'

# s4 = {1, 2, 3, {'a': 'abc'}}
# print(s4)                     # TypeError: unhashable type: 'dict'

s5 = {1, 2, 3, 1, 2, 3, 4, 5}
print(s5)                       # {1, 2, 3, 4, 5}
# ---------------------------------
s6 = (1, 2, 3, (1, 2, 3), [1, 2, 3])
s7 = [(1, 2, 3, (1, 2, 3), [1, 2, 3])]
# print(s6, s7)

# d1 = {[1, 2, 3] : 'abc', }

# d2 = [5, 4, 7, 3, 8, 2, 9, 1]
# d3 = sorted(d2)
# print(d3)       # [1, 2, 3, 4, 5, 7, 8, 9]
# # sort(d2)
#
# z = d2.sort()
# print(z)        # None
# ---------------------------------
# c, d = 10, 10
# print(c == d)   # True
# print(c is d)   # True
# ---------------------------------
# d9 = [5, 7, 3, 6, 2, 9, 1]
# d9.sort()
# print(d9)           # [1, 2, 3, 5, 6, 7, 9]
# k = d9[len(d9)//2]
# print(k)            # 5
# ---------------------------------

# y = 'stuff;thing;junk;'
# z = y.split(';')
# print('after splitting: ', z)   # ['stuff', 'thing', 'junk', '']
# print(len(z))                   # 4
# ---------------------------------

# print(5 != 6)       # True
# ---------------------------------

# print(list(reversed(range(1, 11))))     # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# ---------------------------------

# Mylist = [2, 'Apple', 3.4]
# Mylist[1] = 'orange'
# print(Mylist)           # [2, 'orange', 3.4]
# ---------------------------------

# num_list = [1, 2, 3, 4, 5]
# num_list.remove(2)
# print(num_list)         # [1, 3, 4, 5]
# ---------------------------------


# ---------------------------------

