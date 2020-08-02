# Enter your code here. Read input from STDIN. Print output to STDOUT
# contents of input file at bottom

""" Read from file, create dictionary {k,v}, query it. """

import sys

# initialize list for input
list_of_inputs = []

# create loop to readlines
for line in dict_practice_1.txt:

    # remove trailing space at end of line
    line = line.rstrip('\n')

    # add each line to the list
    list_of_inputs.append(line)

# extract the number of name and number combos
# in list from number on first line
num_of_elements = int(list_of_inputs[0])

# initialize dictionary
phone_bk_dict = {}

# add name, number to phone_bk_dict
for i in range(num_of_elements):
    i += 1

    # find the index of the space between name and #
    space = str(list_of_inputs[i]).find(" ")

    # add name, number to dictionary
    name = (list_of_inputs[i][:space])
    number =(list_of_inputs[i][space + 1:])
    phone_bk_dict[name] = number
    
# query phone_bk_dict for names in list
stop = len(list_of_inputs)
start = num_of_elements + 1

for i in range(start, stop):
    if list_of_inputs[i] in phone_bk_dict:
        print(list_of_inputs[i] + '=' + phone_bk_dict[list_of_inputs[i]])
    else:
        print('Not found')    
    i += 1


# contents of input file
# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry