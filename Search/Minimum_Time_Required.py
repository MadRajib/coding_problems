#!/bin/python3

from math import ceil
import os


# Complete the minTime function below.
def minTime(machines, goal):
    n = len(machines)
    low = 1
    max = goal*max(machines)

    while low < max:
        mid  = (low+max) //2
        count = 0
        for i in range(n):
            count += (mid//machines[i])

        if count < goal:
            low = mid +1
        else:
            max = mid
    return max    
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    # fptr.write(str(ans) + '\n')

    # fptr.close()
