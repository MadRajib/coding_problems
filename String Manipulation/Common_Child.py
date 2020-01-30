#!/bin/python3

import math
import os
import random
import re
import sys

def commonChild():
    s1 = input()
    s2 = input()
    m = len(s1)
    n = m+1
    arr = [[0]*(m+1) for _ in range(2)]
    # print(arr)

    for i in range(1,n):
        cr = i%2
        pr = 1-cr
        for j in range(1,n):
            if s1[i-1] == s2[j-1]:
                arr[cr][j] =  arr[pr][j-1] + 1
            elif arr[pr][j] > arr[cr][j-1]:
                arr[cr][j] = arr[pr][j]
            else:
                arr[cr][j] = arr[cr][j-1]

    return arr[cr][m]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    result = commonChild()
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
