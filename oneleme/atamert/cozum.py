from operator import itemgetter

n=int(input())
P=[]

def cross(p,q,r):
    return ( (p[0]-q[0])*(r[1]-q[1]) - (p[1]-q[1])*(r[0]-q[0]) )

U,L=[],[]
def makeconvex(P):

    global U,L
    U,L=[],[]

    sz=len(P)
    for i in range(sz):
        while ( (len(U)>=2) and (cross(U[-2],U[-1],P[i])<=0) ):
            U.pop()
        U.append(P[i])

    for i in range(sz):
        while ( (len(L)>=2) and (cross(L[-2],L[-1],P[i])>=0) ):
            L.pop()
        L.append(P[i])

def nefretSeviyesi(p1,p2):
    return abs(p1[0]-p2[0])+ abs(p1[1]-p2[1])

def nefretKolik():
    #birbirinden encok nefret eden 2 kisiyi buluyoz

    global U,L
    ans=0
    P,Q=0,0
    sizeU=len(U)
    sizeL=len(L)
    i,j=0,sizeL-1

    #print(sizeU,sizeL)

    while j>0 or i<sizeU-1:

        tmpdist = nefretSeviyesi(U[i],L[j])
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

    global ans

    while(len(P)>1):

        size=len(P)
        tmp=P[:]
        tmp.sort(key=itemgetter(0,1))

        makeconvex(tmp)
        #print(U,"\n",L)

        res = nefretKolik()
        #print(res)

        maxx=max(res)
        #print(maxx)

        disT=nefretSeviyesi(P[res[0]-1],P[res[1]-1])
        #print(disT,"<<<----")

        for i in range(maxx,size+1):
            ans[i]=disT

        count=size-maxx+1

        while count:
            count-=1
            P.pop()

        #print(U,"\n",L,"\n")


    for i in ans[2:n+2]:
        print(i)


def main():


    P.append([310,440,1]) #ata mert -> 310 440
    for i in range(2,n+2):
        name,surname=input().strip().split()
        tx, ty = 0, 0
        for el in name:
            tx += ord(el)
        for el in surname:
            ty += ord(el)

        P.append([tx,ty,i])

    solution()


if __name__ == '__main__':
    main()


"""

4
o guz
bar an
ay ca
bil ge


"""