if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        qrs = input().rstrip().split()
        qr = qrs[0]
        if qr == "insert": 
            arr.insert(qrs[0],qrs[1])
            pass
        elif qr == "print": 
            for j in range(len(arr)):
                print(arr[j],"")
        elif qr == "remove": 
            arr.remove(qrs[0],qrs[1])
        elif qr == "sort": 
            arr.sort()
        elif qr == "pop": 
            arr.pop()
        elif qr == "reverse": 
            arr.reverse()