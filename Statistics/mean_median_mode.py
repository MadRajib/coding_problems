if __name__ == "__main__":
    n = int(input())

    ar = sorted(list(map(int, input().rstrip().split())))
    mean = 0
    median = 0
    mode = 0
    mode = ar[0]
    count = dict()
    for i in range(n):
        elem = ar[i]
        if elem not in count:
            count[elem] = 0

        count[elem] += 1
        if count[mode] < count[elem]:
            mode = elem
        mean += elem
    
    mean /= n
    
    median = (ar[n//2] + ar[-(n//2 +1)] ) / 2

    
    print(mean)
    print(median)
    print(mode)