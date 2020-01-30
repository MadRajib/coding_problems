if __name__ == "__main__":
    n = int(input())

    ar = list(map(int, input().rstrip().split()))
    w = list(map(int, input().rstrip().split()))
    
    mean = round(sum([a*b for a,b in zip(ar,w)])/sum(w),1)
    print(mean)