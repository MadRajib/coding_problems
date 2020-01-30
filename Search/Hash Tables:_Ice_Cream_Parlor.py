#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    need = dict()
    for i in range(1,len(cost)+1):
        if need.get(cost[i-1],0) :
            print(need[cost[i-1]],i)
            break
        else:
            n = money - cost[i-1]
            need[n] = i

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
