#!/bin/python3

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    flag = 'Yes'
    for elem in note:
        if elem not in magazine or magazine.get(elem) <= 0:
            flag = 'No'
            break
        elif elem in magazine: 
            magazine[elem] = magazine[elem] - 1

    print(flag)


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()
    dc = dict()

    for k in magazine:
        if k in dc :
            dc[k] = dc[k]+1
        else:
            dc[k] = 1

    note = input().rstrip().split()

    checkMagazine(dc, note)
