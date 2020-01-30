#!/bin/python3

import os
from bisect import bisect

# Complete the triplets function below.
def triplets(a, b, c):
    a = sorted(set(a))
    b = set(b)
    c = sorted(set(c))
    count = 0
    for e in b:
        c1 = bisect(a,e)
        
        c2 = bisect(c,e)

        count+= c1*c2

    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    # fptr.write(str(ans) + '\n')

    # fptr.close()
