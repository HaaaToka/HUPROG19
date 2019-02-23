from collections import defaultdict,Counter
from operator import itemgetter
import os
from time import time
a=time()


n=0
P=[]

def cross(p,q,r):
    return ( (p[0]-q[0])*(r[1]-q[1]) - (p[1]-q[1])*(r[0]-q[0]) )

U,L=[],[]
def makeconvex(P):

    global U,L
    U,L=[],[]

    sz=len(P)
    for i in range(sz):
        while ( (len(U)>=2) and (cross(U[len(U)-2],U[len(U)-1],P[i])<=0) ):
            U.pop()
        U.append(P[i])

    for i in range(sz):
        while ( (len(L)>=2) and (cross(L[len(L)-2],L[len(L)-1],P[i])>=0) ):
            L.pop()
        L.append(P[i])

def dist(p1,p2):
    return abs(p1[0]-p2[0])+ abs(p1[1]-p2[1])

def GetMaxPair():

    global U,L
    ans=0
    P,Q=0,0
    sizeU=len(U)
    sizeL=len(L)
    i,j=0,sizeL-1

    #print(sizeU,sizeL)

    while j>0 or i<sizeU-1:

        tmpdist = dist(U[i],L[j])
        #print(tmpdist,i,j)
        if tmpdist>ans:
            P=i
            Q=j
            ans=tmpdist
        if i==sizeU-1:
            j-=1
        elif j==0:
            i+=1
        elif ( (U[i+1][1]-U[i][1])*(L[j][0]-L[j-1][0]) > (U[i+1][0]-U[i][0])*(L[j][1]-L[j-1][1]) ):
            i+=1
        else:
            j-=1
        #print("---->>>",i,j)

    return [U[P][2],L[Q][2]]

ans=[0]*750005

def solution():

    global ans,P,U,L

    while(P.__len__()>1):

        size=len(P)
        tmp=P[:]
        tmp.sort(key=itemgetter(0,1))

        makeconvex(tmp)
        #print(U,"\n",L)

        res = GetMaxPair()
        #print(res)

        maxx=max(res)
        #print(maxx)

        disT=dist(P[res[0]-1],P[res[1]-1])
        #print(disT,"<<<----")

        for i in range(maxx,size+1):
            ans[i]=disT

        count=size-maxx+1

        while count:
            count-=1
            P.pop()

        print(U,"\n",L,"\n")




def main():

    global ans, n, P, U, L

    inputs = os.listdir("./input")

    for inp in inputs:
        ans=[0]*500005
        P,U,L=[],[],[]

        inputfile = open("input/"+inp,"r")
        number=inp[5:7]
        out = open("output/output" + number + ".txt", "w")
        print("su an " + number + " nolu outputu hazirliyorum... gecen sure: " + str(time() - a))

        n=int(inputfile.readline())

        P.append([310,440,1])
        for i in range(2,n+2):
            xl,yl=inputfile.readline().strip().split()
            x,y=0,0
            for el in xl:
                x+=ord(el)
            for el in yl:
                y+=ord(el)

            P.append([x,y,i])

        solution()

        #print(0,file=out)
        for elem in ans[2:n+2]:
            print(elem,file=out)



if __name__ == '__main__':
    main()


"""

5
20 20
40 30
35 35
0 10
-170 1000000000

"""