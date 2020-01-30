#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    print(a,b)
    if len(b) < 1 :
        for i in range(len(a)):
            if ord(a[i]) < 91: return 'NO'
        return 'YES'
    if len(a) < 1 : return 'NO'
    
     
    if ord(a[0]) > 96 and a[0].capitalize() != b[0]:
        return abbreviation(a[1:],b)
    elif a[0] == b[0] or a[0].capitalize() == b[0]:
        return abbreviation(a[1:],b[1:])
    else:
        return 'NO'
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
