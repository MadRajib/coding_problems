#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0
    s = []
    for e in contests:
        
        if e[1]:
            s.append(e[0])
        else:
            luck += e[0]
    s = sorted(s,reverse = True)
    for e in range(len(s)):
        if k > 0:
            luck +=s[e]
            k -=1
        else:
            luck -=s[e]

        
        
    return luck

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
