#!/bin/python3

import os


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []
    l = [0] *(n+1)
    for _ in range(m):
        arr = list(map(int, input().rstrip().split()))

        l[arr[0] - 1] += arr[2]

        if arr[1] < (n+1):
            l[arr[1]] -= arr[2]
    
    max_ = l[0]
    x = 0
    for i in range(n):
        x += l[i]
        if(max_<x):
            max_ = x

    result = max_

    fptr.write(str(result) + '\n')

    fptr.close()
