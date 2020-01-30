#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the minimumPasses function below.
def minimumPasses(m, w, p, n):
    nCandies = m * w
    nPass = 1
    while nCandies < n:
        nPass = nPass + 1 
        case1 = m*w
        temp = 0

        if nCandies >= p :
            c = nCandies//p

            # if m == 1 and w == 1:
            #     m = 2
            #     c = c - 1 if c - 1 > 0 else 0
            #     w = 2 if c > 0 else 1
            #     c = c - 1 if c - 1 > 0 else 0
            # elif m == 1:
            #     m = 2
            #     c = c - 1 if c - 1 > 0 else 0
            # elif w == 1:
            #     w == 2
            #     c = c - 1 if c - 1 > 0 else 0
            
            
            a_1 = (m + c)*w
            a_2 = m*(w + c)
            a = a_2 if a_2 > a_1 else a_1
            temp = (nCandies - c*p) + a
        
            

        if nCandies + case1 >= temp:
            nCandies = nCandies + case1
        else:
            nCandies = temp
            
    print(nPass)
    
    return nPass
          

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mwpn = input().split()

    m = int(mwpn[0])

    w = int(mwpn[1])

    p = int(mwpn[2])

    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    # fptr.write(str(result) + '\n')

    # fptr.close()
