#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    m = 999999999
    arr = sorted(arr)
    for i in range(len(arr)-1):
            s = abs(arr[i] - arr[i+1])
            if s < m:
                m = s
            
    return m
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()