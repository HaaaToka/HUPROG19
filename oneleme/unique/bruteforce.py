from collections import Counter

n,q = map(int,input().strip().split())
arr=list(map(int,input().strip().split()))
for _ in range(q):
    que = input().strip().split()
    l,r=int(que[1]),int(que[2])
    if que[0]=="F":
        cnt = Counter(arr[l-1:r])
        ans=0

        for key,value in cnt.items():
            if value==1:
                ans+=1
        print(ans)

    elif que[0]=="U": #
        inc = int(que[3])
        for i in range(l,r+1):
            arr[i-1]+=inc

    elif que[0]=="S":
        same = int(que[3])
        for i in range(l,r+1):
            arr[i-1]=same
        

"""

10 7
1 2 3 1 4 5 1 2 3 2
F 1 10
U 1 10 1
F 4 7
F 8 10
S 2 7 1
F 1 5
F 2 9

"""
