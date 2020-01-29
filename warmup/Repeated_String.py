#!/bin/python3

import os


# Complete the repeatedString function below.
def repeatedString(s, n):
    ln = len(s)
    r = n % ln

    c_a =0
    c_r = 0
    for i in s:
        if i == 'a' or i == 'A':
            c_a+=1
    for i in range(r):
        if s[i] == 'a':
            c_r += 1
    
    return (int(n/ln))*c_a + c_r
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
