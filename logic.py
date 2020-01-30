def isPalindrome(s):
    for i in range(len(s)//2):
        if s[i] !=s[-(i+1)]:
            return False
    return True

    
def substrCount(n, s):
    c = 0
    for i in range(n):
        for j in range(i+1,n+1):
            sub = s[i:j]
            print(sub)
    return c


def merge(start,mid,end,array):
    i = start
    j = mid + 1
    temp = [0]*(end-start+1)
    l = 0
    for k in range(end-start+1):
        if i>mid :
            temp[l] = array[j]
            l += 1
            j += 1
        elif j > end:
            temp[l] = array[i]
            l += 1
            i += 1
        elif array[i] < array[j]:
            temp[l] = array[i]
            l += 1
            i += 1
        else:
            temp[l] = array[j]
            l += 1
            j += 1


    for k in range(l):
        array[start] = temp[k]
        start += 1
    

def merge_sort(s,e,array):
    if (s<e) :
        mid = (s + e)//2
        merge_sort(s,mid,array)
        merge_sort(mid+1,e,array)
        merge(s,mid,e,array)