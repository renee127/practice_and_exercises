print('use type to find type & notice str to list to str')
str_A = ('abc')
my_tuple = (9, 9, 3, 4)
list_B = list('def')
str_B = str(list_B)
print(type(my_tuple), my_tuple)
print(type(list_B), list_B)
print(type(str_A), str_A)
print(type(str_B), str_B)
print(' ')
print('to get sense of total length of line')
print( '0' * 79 )
print('use dir() to find out the attributes')
print(dir(list_B))
print('dir() also prints out methods in a module')
import time
print(dir(time))