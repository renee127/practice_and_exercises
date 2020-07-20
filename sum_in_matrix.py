#!/bin/python3
""" Calculate sum of elements from shape in matrix. """

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    #initialize values     
    row = 0
    
    # set max_sum to first value incase sums are all negative
    # tried max_sum = 0, max_sum = None - don't work
    max_sum = arr[0][0] + arr[0][1] + arr[0][2] \
            + arr[1][1] + arr[2][0] + arr[2][1] +   \
            arr[2][2]

    # another option is to append running_sum to 
    # a list and then get the max at the end...
    # but which way is faster        
 
    running_sum = 0
    # loop through rows and columns 
    for row in range(4):
        for col in range(4):
            # find sum of hourglass shape (3,1,3)
            running_sum = arr[row][col] + arr[row][col+1] + arr[row][col+2] \
            + arr[row + 1][col+1] + arr[row+2][col] + arr[row+2][col+1] +   \
            arr[row+2][col+2]

            col += 1

            # find max sum out of running sums           
            if running_sum > max_sum:
                max_sum = running_sum

        row += 1
    print(max_sum)