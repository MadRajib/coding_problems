#!/bin/python3

import os

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    ln = len(c)
    jump = 0
    i = 0
    
    while i<ln :
        if i+2<ln and c[i+2] == 0:
            i+=2
        else:
            i+=1
        jump+=1

    return jump - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
