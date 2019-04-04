
graph=[[] for _ in range(510)]
indeg=[0]*510
outdeg=[0]*510
lanetli=[]
buyulu=[]
dp=[0]*510
a=[[0 for _ in range(260)] for __ in range(260)]
P=10**9+7

def dfs(x):

    if(dp[x]!=-1):
        return dp[x]

    ans=0
    for i in range(len(graph[x])):
        ans+=dfs(graph[x][i])
        if ans>=P:
            ans-=P
    dp[x]=ans
    return dp[x]

def power(x,n):
    if(n == 0):
        return 1
    y = power(x,n//2)
    y = y * y % P
    if(n%2 == 1):
        y = y * x % P
    return y


def func():
    flag=False

    # print("DDD",D)
    t=0
    for j in range(D):
        t=j
        while t<D:
            if a[t][j]!=0:
                break
            t+=1
        if t==D:
            return 0
        if t!=j:
            # print("girdim")
            flag=not flag
            for k in range(D):
                a[t][k],a[j][k]=a[j][k],a[t][k]

        for i in range(j+1,D):
            coef = (P-a[i][j])*power(a[j][j],P-2)%P
            # print("i ",i,"coef",coef)
            for k in range(j,D):
                a[i][k]=(a[i][k]+a[j][k]*coef)%P

    # print("flag",flag)
    if flag:
        ans=P-1
    else:
        ans=1

    for i in range(D):
        ans=ans*a[i][i]%P

    return ans


n,m=map(int,input().strip().split())

for _ in range(m):
    x,y=map(int,input().strip().split())
    x-=1
    y-=1
    indeg[y]+=1
    outdeg[x]+=1
    graph[y].append(x)

for i in range(n):
    if(indeg[i]>0 and outdeg[i]==0) :
        lanetli.append(i)
    if (indeg[i] == 0 and outdeg[i] > 0):
        buyulu.append(i)

D=len(lanetli)
# print("DD",D)
# print(len(graph[0]))
for i in range(D):
    for j in range(n):
        dp[j]=-1
    dp[buyulu[i]]=1
    for j in range(D):
        a[i][j]=dfs(lanetli[j])

# for elem in a:
#     print(elem)


ans=func()
# print("ans",ans)

flag=False
for i in range(n):
    if indeg[i]==0 and outdeg[i]==0:
        cnt1,cnt2=0,0
        for j in range(D):
            if lanetli[j]<i:
                cnt1+=1
        for j in range(D):
            if buyulu[j] < i:
                cnt2 += 1
        if cnt1%2!=cnt2%2:
            flag=not flag
if flag:
    ans=(P-ans)%P
print(ans)
