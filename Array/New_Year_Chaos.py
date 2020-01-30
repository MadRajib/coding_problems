#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the minimumBribes function below.
def minimumBribes(q):
    swaps = 0
    for i in reversed(range(len(q))):
        if (-(i+1) + q[i]) > 2 :
            print("Too chaotic ")
            return 
        
        for j in range(max(0,q[i]-2),i):
            
            if q[j] > q[i]:
                swaps +=1

    print(swaps)
        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
