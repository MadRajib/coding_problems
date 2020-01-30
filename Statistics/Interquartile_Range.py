if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    freq = list(map(int, input().split()))

    s = []
    for i in range(n):
        s += [data[i]] * freq[i]   
    ar = sorted(s)
    n = len(s)

    m = n//2
    im = m+1 if n%2 else m

    Q1 = (ar[m//2] + ar[-im-(m//2 +1)] ) / 2
    Q2 = (ar[n//2] + ar[-(n//2 +1)] ) / 2
    Q3 = (ar[im+m//2] + ar[-(m//2 +1)] ) / 2   
        
        
    print(round(Q3 - Q1,1))