#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Answer MUST be recursive
        
    # check single digits
    if k == len(n) == 1:
        return int(n)

    result = 0
    for num in n:
        res += int(num) # Get new sum

    return superDigit(str(result*k),1) # Use recursion to get down to one digit
            

result = superDigit(148, 3)
print(result)
