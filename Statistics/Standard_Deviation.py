from math import sqrt
if __name__ == "__main__":
    n = int(input())

    ar = list(map(int, input().rstrip().split()))    
    m=0
    for e in ar:
        m+=e
    m = m/n
    s = 0
    for e in ar:
        s+= (e - m)**2
    s = sqrt(s/n)
    print(round(s,1))