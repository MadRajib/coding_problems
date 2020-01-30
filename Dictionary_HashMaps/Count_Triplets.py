#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    dc_1 = dict()
    dc_2 = dict()
    count = 0
    for elem in reversed(arr):
        
        
        if elem*r in dc_2:
            count += dc_2[elem*r]        

        if elem*r in dc_1:
            dc_2[elem] =  dc_1.get(elem*r) + dc_2.get(elem,0)  


        dc_1[elem] = dc_1.get(elem,0) + 1

        
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)
    print(ans)

    # fptr.write(str(ans) + '\n')

    # fptr.close()
