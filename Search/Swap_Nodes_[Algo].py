#!/bin/python3

import os
import sys


class Node:
    def __init__(self,vl,l =None,r=None):
        self.l  = l
        self.r = r
        self.v = vl

class Solve:
    def __init__(self):
        self.depth = None
        self.r = []

    def swapNodes(self,indexes, queries):
        n = len(indexes)
        self.depth = [None]*(n+1)
        tree = [None]* (n +1)
        for i in range(1,n+1):
            tree[i] = Node(i)
            self.depth[i] = []
        c = 1
        for l,r in indexes:
            if l != -1:
                tree[c].l = tree[l] 
                
            if r != -1:
                tree[c].r = tree[r]
            c+=1

        self.dfa(tree[1],1)



        for i in range(len(queries)):
            k = queries[i]
            h = k
            while h <= n :
                for j in range(len(self.depth[h])):
                    e = self.depth[h][j]
                    temp = tree[e].l
                    tree[e].l = tree[e].r
                    tree[e].r = temp

                h += k
        self.inorder(tree[1])
        return self.r
        
    def dfa(self,node,y):
        if node is None:
            return
        self.depth[y].append(node.v)
        self.dfa(node.l ,y+1)
        self.dfa(node.r ,y+1)

    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.l)
        self.r.append(node.v)
        self.inorder(node.r)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = Solve().swapNodes(indexes, queries)
    # print(result)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
