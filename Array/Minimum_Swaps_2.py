#!/bin/python3

import os



# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    vsNode = [0]*len(arr)
    swaps = 0
    for i in range(len(arr)):
        if vsNode[i] != 1:
            q = arr[i]
            vsNode[i] = 1
            while(q != arr[q-1]):
                swaps+=1
                q = arr[q-1]
                vsNode[q - 1] = 1
                if q == arr[i] :
                    swaps-=1
                    break
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
