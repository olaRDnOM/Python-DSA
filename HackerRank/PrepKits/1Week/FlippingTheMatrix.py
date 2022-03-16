#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    sum = 0
    quadrant_size  = len(matrix)/2

    for i in range(0,quadrant_size):
        for j in range(0,quadrant_size):
            value1 = matrix[i][(quadrant_size*2)-j-1]
            value2 = matrix[i][j]
            value3 = matrix[(quadrant_size*2)-i-1][j]
            value4 = matrix[(quadrant_size*2)-i-1][(quadrant_size*2)-j-1]

            sum += max(value1, max(value2, max(value3, value4)))

    return sum
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
