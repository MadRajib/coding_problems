#!/bin/python3


import os

# Complete the countInversions function below.
def inversions(arr):
    n = len(arr)
    if n==1:
        return 0
    n1 = n//2
    n2 = n - n1
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    ans = inversions(arr1) + inversions(arr2)
    i1 = 0
    i2 = 0
    for i in range(n):
        ''' Logic:
            if some elements in 1st array is smaller or equal to element in 2nd 
            array that means current elem of first array was greater than i2 elements 
            of 2nd array!
        '''
        if i1 <n1 and (i2>=n2 or arr1[i1]<=arr2[i2]):
            arr[i] = arr1[i1]
            ans += i2
            i1 += 1 
        elif i2 < n2:
            arr[i] = arr2[i2]
            i2 += 1
    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = inversions(arr)

        # fptr.write(str(result) + '\n')

    # fptr.close()
