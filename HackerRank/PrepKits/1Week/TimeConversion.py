#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time_of_day = s[-2:]
    hour = s[:2]

    if time_of_day == 'PM' and hour != '12':
        hour = int(hour) + 12
        s = str(hour) + s[2:8]
    elif time_of_day == 'AM' and hour == '12':
        hour = '00'
        s = hour + s[2:8]
    else:
        s = s[:8]
        
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
