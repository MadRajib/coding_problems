#!/bin/python3
import os


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a1 = [0]*26

    for e in a:
        i = ord(e) - 97
        a1[i] += 1
        
    for e in b:
        i = ord(e) - 97
        a1[i] -= 1

    
    c = 0
    for i in range(26):
        c += abs(a1[i]) 
    return c
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)
    print(res)
    # fptr.write(str(res) + '\n')

    # fptr.close()
