#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min = 0
    max = 0
    i = 0

    for i in range(len(arr)):
        test = list(arr)
        test.pop(i)
        sum = 0

        for j in test:
            sum += j
            
        if max != 0 and sum > max:
            max = sum
        elif min != 0 and sum < min:
            min = sum
        elif min != 0 and (sum < max or sum > min ):
            next
        else:
            min = sum
            max = sum     

    print(str(min) + " " + str(max))
            

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
