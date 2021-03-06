#!/bin/python3
# John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
# Given an array of integers representing the color of each sock, determine how many pairs of socks
#  with matching colors there are.

# For example, there are n = 7 socks with colors ar = [1,2,1,2,1,3,2].
# There is one pair of color 1  and one of color 2. There are three odd socks left, one of each color.
#  The number of pairs is 2.

import os


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sum = 0
    b = [0] * 1000
    for i in ar:
        b[i]+=1
        if b[i] % 2 == 0 :
            sum+=1

    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()