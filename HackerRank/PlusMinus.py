#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_sum = 0
    neg_sum = 0
    zero_sum = 0

    for i in arr:    
        if i > 0:
            pos_sum+=1
        elif i < 0:
            neg_sum+=1
        else:
            zero_sum+=1 
            
    print(pos_sum/len(arr))
    print(neg_sum/len(arr))
    print(zero_sum/len(arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
