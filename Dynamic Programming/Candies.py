#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    candies = [0]*n
    candies[0] = 1
    for i in range(1,n):
        candies[i] = (candies[i-1]+1) if arr[i] > arr[i-1] else 1
    for i in reversed(range(n-1)):
        candies[i] = (candies[i+1]+1) if arr[i] > arr[i+1] and candies[i] <= candies[i+1] else candies[i] 
    return sum(candies)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
