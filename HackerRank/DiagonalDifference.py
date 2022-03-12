#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

#2D array example
#   1 2 3
#   4 5 6
#   9 8 9 


def diagonalDifference(arr):
    array_length = len(arr)
    a,b = 0,0

    for i in range(0,array_length):
        a += arr[i][i] #Gets total of first diagonal of array
        b += arr[i][array_length-1-i] #Gets total of second diagonal of array

    return abs(a-b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
