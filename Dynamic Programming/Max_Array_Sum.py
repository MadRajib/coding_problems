#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
# def maxSubsetSum(arr):
#     n = len(arr)
#     a = [[0]*n for _ in range(n)]
#     for i in range(n):
#         a[i][i] = arr[i]
    
#     for i in reversed(range(n)):
#         for j in range(i):
#             r_inx = i-1-j
#             c_inx = (n-1) -j
#             a[r_inx][c_inx] = max(a[c_inx][c_inx],    a[c_inx][c_inx]+a[r_inx][c_inx-2],    a[r_inx][c_inx-1])

#     return a[0][n-1]

def maxSubsetSum(arr):

    mx = [arr[0],max(arr[:2])]

    for i,e in enumerate(arr[2:],2):
        mx[i%2] = max(e,mx[i%2]+e,mx[(i-1)%2])
    
    return max([0] + mx)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
