#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):

    dc = dict()
    count = 0
    for i in range(len(arr)):
        e = arr[i]
        c = dc.get(e,0)
        if c:
            count += c
        
        dc[e+k] = dc.get(e+k,0) + 1
        dc[e-k] = dc.get(e-k,0) + 1
        

    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
