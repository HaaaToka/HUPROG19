n,k = map(int,input().split())
sm = list(map(int,input().split()))
lis = [10**4 for i in range(n)]

def tarik_sort(n, k, sm, lis):
    for i in range(k-1):
        ix,t = map(int,input().split())
        ix = ix-1
        lis[ix] = t 
        for e in range(ix-k,-1,-k):
            lis[e] = lis[e+k] - (sm[e+1] - sm[e])
        for e in range(ix+k,n,k):
            lis[e] = lis[e-k] + (sm[e-k+1] - sm[e-k])
    for ix in range(k):
        if lis[ix] == 10**4:
            #print(ix)
            #print(lis[ix])
            #print(sum(lis[:k])-10**4)
            lis[ix] = sm[0]-(sum(lis[:k])-10**4)
            
            for e in range(ix+k,n,k):
                lis[e] = lis[e-k] + (sm[e-k+1] - sm[e-k])
            break
    return lis

