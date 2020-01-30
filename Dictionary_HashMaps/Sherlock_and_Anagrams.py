#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    ln = len(s)
    dc = dict()
    count = 0 

    # Calculate all the subsets and identify them using no of charaterers in it.
    for i in range(ln):
        for j in range(i+1,ln+1):
            sub = s[i:j]
            lt= [0]*26

            for e in sub:
                index = ord(e)-97
                lt[index] = lt[index] +1

            st = "".join(map(str,lt))
            if st not in dc:
                dc[st] = 0
            else:
                dc[st] = dc[st] + 1
                count = count + dc[st]
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
