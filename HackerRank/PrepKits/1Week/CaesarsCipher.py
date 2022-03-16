#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    k = k % 26 #Modulo for annoying cases where k > 26
    string1 = alphabet[:k]
    string2 = alphabet[k:]
    cipher = string2 + string1
    encrypted_output = ''

    for i in s: #Loop through input
        if i.isalpha():
            for j in range(0,len(alphabet)): #Try to find index in alphabet
                if i.lower() == alphabet[j]: #Check if input char and alphabet char are the smae
                    index = j
                    if i.islower(): #Check for proper case
                        encrypted_output += cipher[index]
                    else:
                        encrypted_output += cipher[index].upper()
        else:
            encrypted_output += i #Just add character if its not a letter

    return encrypted_output
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
