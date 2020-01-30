if __name__ == "__main__":
    n = int(input())

    ar = sorted(list(map(int, input().rstrip().split())))    
    m = n//2
    im = m+1 if n%2 else m

    Q1 = (ar[m//2] + ar[-im-(m//2 +1)] ) / 2
    Q2 = (ar[n//2] + ar[-(n//2 +1)] ) / 2
    Q3 = (ar[im+m//2] + ar[-(m//2 +1)] ) / 2   
        
        
    print(int(Q1))
    print(int(Q2))
    print(int(Q3))