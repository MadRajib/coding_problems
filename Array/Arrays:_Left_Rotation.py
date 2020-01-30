#!/bin/python3

import os


# Complete the rotLeft function below.
def rotLeft(a, d):
    b = [0] * len(a)
    i = 0
    for j in range(d,len(a)):
        b[i] = a[j]
        i+=1

    for j in range(d):
        b[i] = a[j]
        i+=1

    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
