#!/bin/python3

import math
import os
import random
import re
import sys

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

def solution(nums):
    running_sum = []
    for i in range(0,len(nums)):
        sum = 0
        for j in range(i+1):
            sum += nums[j]
        running_sum.append(sum)
    print(running_sum)

nums = [1,2,3,4]
solution(nums)