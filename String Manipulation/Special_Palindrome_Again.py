#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.

'''
Approach: 
 1st pass:we will save letters and their frequencies and plus count case 1 cases! 
 
 create a list of alphabets and how many times they occurs consiquitively!
 eg aaabaa 
    [
        [a,3], a occurs 3 times
        [b,1], b 1 times
        [a,2]  a again 2 times
    ]
--------------------------------------------------------------------------------------
note: number of subsets for a string of n is n(n+1)/2
--------------------------------------------------------------------------------------
for case 1: aaa, bbbb, ie same letter strings:
    we will use n(n+1)/2 formula and save it to the count, in the 1st pass whn we append
    to the list

2nd pass: we will count case 2 strings!
    for this we will search for patters which has:
        same letters at i and i+2
        and only 1 letter occurs at position i+1
        if we find some case then we will take the min of 
        frequencies from 1st and last part.
        eg. a3 d a4
        we will take 3 . and add it to count. since
        aaadaaaa has 3 pallindroe inside it.
            1.aaadaaa
            2. aadaa
            3.  ada



'''
def substrCount(n, s):
    count = 0
    c = 1
    prev = s[0]
    cn = []
    l = 0
    # 1st pass
    for i in range(1,n):
        if prev == s[i]:
            c+=1
        else :
            cn.append([prev,c])
            count += (c*(c+1))//2
            c=1
            prev = s[i]
            l +=1


    cn.append([prev,c])
    count += (c*(c+1))//2
    # end of 1st pass
    
    # 2nd pass: 
    for i in range(l-1):
        
        if cn[i][0] == cn[i+2][0] and cn[i+1][1] == 1:
                count += min(cn[i][1],cn[i+2][1])
    # end of 2nd pass
    return count
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    
    result = substrCount(n, s)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
