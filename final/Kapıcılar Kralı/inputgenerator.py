
import os
from random import randint
from time import time
a=time()

"""

1<=N<=500
1<=M<=10**5

"""

testcase=20

buyulu,lanetli,ikisi=[],[],[]

def creater(n):
    global buyulu,lanetli,ikisi

    buyulu=[i for i in range(1,n)]
    ik=randint(0,n//2)
    while ((n-ik)%2!=1 or ik>(n-ik)//2):
        ik=randint(0,n//2)
    ikisi=buyulu[-ik:]
    buyulu=buyulu[:-ik]
    lanetli=buyulu[:len(buyulu)//2]
    buyulu=buyulu[len(buyulu)//2:]

    # print(lanetli,len(lanetli),"\n",buyulu,len(buyulu),"\n",ikisi)

    if(len(lanetli)!=len(buyulu)):
        return False
    return True


def printer(M):

    edge=[]

    lnby=len(buyulu)
    #garanti 1-1 hepsi için ilk
    for i in range(lnby):
        edge.append([buyulu[i],lanetli[i]])

    for i in range(M-lnby):
        x,y=randint(0,lnby-1),randint(0,lnby-1)
        edge.append([buyulu[x],lanetli[y]])

    if len(edge)!=M:
        print("ananna",len(edge),M)

    return edge


for i in range(testcase):
    print(i,". input oluşturuluyor...",time()-a)
    a=time()

    out=open("./input/input"+str(i).zfill(2)+".txt","w")

    buyulu, lanetli, ikisi = [], [], []

    N,M=0,0

    if 0<=i<5:
        N=randint(5,25)
        M=randint(N//2,10**2)

    elif 5<=i<10:
        N=randint(50,200)
        M=randint(N**2,max(N**2,5*10**3))

    elif 10<=i<15:
        N=randint(300,500)
        M=randint(N*50,min(N**2,10**5))

    elif 15<=i<20: #edge cases
        N=randint(499,500)
        M=randint(10**5-1,10**5)


    print(N, M, file=out)
    while (not creater(N)): continue
    edges = printer(M)

    for ed in edges:
        print(*ed,file=out)


