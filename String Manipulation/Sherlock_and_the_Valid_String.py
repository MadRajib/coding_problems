#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    dc = [0]*26
    for e in s:
        i = ord(e) -97 
        dc[i] +=1
    s = dict()
    for i in range(26):
        if dc[i]:
            s[dc[i]] = s.get(dc[i],0) + 1
    



    # Create dict consiting of unique elements and their frequencies
    # if dict lenght is 1 e.i there is only same frequencies, send "yes"
    # if dict has lenght more than 2 i.e there are more than 2 diffrent freq, send "no"
    l = len(s)
    if l == 1:
        return 'YES'
    elif l > 2:
        return 'NO'
    else:
    # if there are two types of diffrent frequencies then
    # get the max number of occuring frequeny and its frequency 
    # same for the min
        mn = 9999999
        mx = 0
        mxi = 0
        mni = 0
        # print(s)
   
    
        for i,v in s.items():
            if mx < v:
                mx = v
                mxi = i
            if mn >= v:
                mn = v
                mni = i
        
    # if there is only one min frquency and if it 1 then send "yes"
    # if there is only one min frequency and if its not one than if it differets from mx
    # frequency by 1 then send "yes"


        if mn == 1 and (mni == 1 or abs(mxi-mni) == 1):
            return 'YES'
    # if no of max frequency are more than one or max frequency and min frequency dont differ 
    # by 1 then say no
        if mx > 1 or mxi-mni > 1:
            return 'NO'

        return 'YES'
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
