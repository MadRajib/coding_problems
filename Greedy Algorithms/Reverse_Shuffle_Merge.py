#!/bin/python3

import math
import os
import random
import re
import sys
'''
 suppose a string S = ababsdabsdabsdabd, and we have to find A.
 we know that s =  merge(reverse(A),shuffle(A)).
   here reverse() reverses the string and shuffle() shuffles the string 
   and merge() merge them both wihtout disturbing the order of the characters.
 
 1st obs:
   since once the string is reversed and next is shuffled and then merged. that means
   i.e len(S) = 2 * len(A)
 2nd obs: 
   since merge() doesnt distrub the relative charater position that means
   our string A is in S in revervesed order (Why revrse order since A is reversed and then merged 
   with the shuffle A)
   That means if we reverse(S) {say s'} or s' has our stirng A as its subsequence.
   now its just matter of fact to find the subsequence.
 
   there can be many subsequence i.e there can be many valid A in s' , but we are required to find 
   the lexically sorted string.
 
 
 
 Solution :
  we will travers s' and find the lexically sorted A . 
       
  
   we have two arrays 
       1. Add[] -> # times we can add a charater in A
       2. Skip[] -> # times we can skip a character in S
       
       since S is 2*A , i.e we have to include characters in S only half of the time and other half we have 
       to skip.
   we have a stack 
       r[] -> it represent A.,also used for backtracking
    
 Approach:
       * create a Add[26] arry which hold frequencies of the characters
       * half each freuency since we can include each char only half the #time they appear in S
       * That also means we can skip half ot the chars of s. 
       * So copy add[26] which was halfed in Skip[26] array 
    
    now 
    for every char in s'
       take the first char in s' 

        * if we encounter char in s' that is smaller to top off the stack(e.i previous smaller char)
            check if we can skip the top of the stack 
            if yes:
                then skip it.
                increment the add[for the top of sstack char] by 1.
                and reduce the skip[for the top of sstack char] by 1.
            keep on poping the stack untill top of the stack can be skipped and top of stack is greater
            than current char in s'

        * if we can add it , then push into the stack e.i if add[charr] >0

            * reduce the add[char] by 1 ( since we can now add one less of that char)
        * else we have used all the char and further char has to be skipped
            * reduce skip[char] by 1,

    return r
'''            



def reverseShuffleMerge(s):
    add = [0]*26
    skip = [0]*26

    n = len(s) 
    for i in range(n):
        inn = ord(s[i]) - 97
        add[inn] += 1
   
    for i in range(26):
        add[i] = add[i] //2
        skip[i] = add[i]


    r = []
    for i in reversed(range(n)):
        inn = ord(s[i]) - 97
        while len(r)>0 and r[-1] > s[i] and add[inn]>0 and skip[ord(r[-1]) - 97]> 0:
             t = ord(r.pop()) -97
             add[t]+=1
             skip[t] -=1
             
        if add[inn] > 0:
            r.append(s[i]) 
            add[inn] -=1
        else:
            skip[inn] -=1

    return "".join(r)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
