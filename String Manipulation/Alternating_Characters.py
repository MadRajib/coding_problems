#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
# def alternatingCharacters(s):
#     a = [0,0]
#     c=0
#     for e in s:
#         o = ord(e)
        
#         if a[o-65] + 1 == 2:
#             c+=1
#         else:
#            a[o-65] = 1

#         a[66-o] = 0 
#     return c
def alternatingCharacters(s):
    c = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            c+=1
    return c

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)
        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
