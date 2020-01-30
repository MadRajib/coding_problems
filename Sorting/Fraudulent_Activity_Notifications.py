#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d,n):
    alerts = 0
    freq = [0]*201

    for v in expenditure[:d]:
        freq[v] += 1

    for i,exp in enumerate(expenditure[d:]):
        
        median=0
        cf = 0
        if d%2:
            for j,xp  in enumerate(freq):
                cf += xp
                if cf > d/2:
                    median = j
                    break
        else:
            sm=0
            for j,xp  in enumerate(freq):
                cf += xp
                if cf >= d/2 and sm==0:
                    sm+=j

                if cf > d/2:
                    sm+=j
                    break
            median = sm/2


        if exp >= 2*median :
            alerts +=1
        freq[expenditure[i]] -= 1
        freq[exp] +=1

    return alerts
            


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d,n)
   
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
