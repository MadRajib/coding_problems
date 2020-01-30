#!/bin/python3

import os

# Complete the twoStrings function below.
# Using sets
def twoStrings(s1, s2):
    if s1 & s2 == set() :
        return 'NO'
    return 'YES'
def twoStrings_(s1,s2):
    for k in set('abcdefghijklmnopqrstuvwxyz'):
        if s1.find(k) > -1 and s2.find(k)> -1:
            return 'YES'


    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s11 = set(s1)

        s2 = input()
        s22 = set(s2)

        result = twoStrings_(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
