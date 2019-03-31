
"""

1<k<10**3
1<n<10**6
1<=m<n
-10**6<=Ai<=10**6
1<=Si<=10**3


"""


n,m,k = map(int,input().strip().split())
if not (1<k<10**3 or 1<n<10**6 or 1<=m<n):
    print("1Constraints")

S=list(map(int,input().strip().split()))
S.insert(0,0)
for elem in S[1:]:
    if not 1<=elem<=10**3:
        print("2Constraints")

ans=[0]*(n+1)
Iset=[0]*(k+1)
for _ in range(k-1):
    Ii,Ai = map(int,input().strip().split())
    if not( 0<Ii<n+1 or -10**6<Ai<10**6 ):
        print("3constraints")
    if Ii%k==0: Iset[-1]+=1
    else: Iset[Ii%k]+=1
    ans[Ii]=Ai
    t=Ii
    while t-k>0:
        ans[t-k]=ans[t]-(S[t-k+1]-S[t-k])
        t-=k
    t=Ii
    while t+k<n:
        ans[t+k]=ans[t]+(S[t+1]-S[t])
        t+=k

# print("\nSS-->>",S)
# print("Iset-->> ",Iset[1:])
# print("ANS -->>",ans[1:])

missing=0
lnIset=0
for i in range(1,len(Iset)):
    if Iset[i]==0:
        missing=i
        continue
    lnIset+=1

if lnIset!=k-1:
    print("4Constraints")

# print("missinng -> ",missing)
parca=1
while parca+k<n+1:
    # print("\ti",missing,"S[missing-1]",S[parca],"sum()",sum(ans[parca:parca+k]),"<<<>>>",parca+1,"-",parca+k)
    ans[missing]=S[parca]-sum(ans[parca:parca+k])
    missing+=k
    parca+=k

# print("ANS -->>",ans[1:])
# print("8484  ",ans[84])


kalanlar=n%k
if kalanlar==0:
    kalanlar+=k
# print("kalanalr",kalanlar)
while kalanlar>0:
    ans[n-kalanlar+1]=0
    # print("\t i",n-kalanlar+1,"<<>>",ans[n-kalanlar+1-k]," - ", S[-kalanlar]-S[-kalanlar-1])
    ans[n-kalanlar+1]= ans[n-kalanlar+1-k]+ ( S[-kalanlar]-S[-kalanlar-1] )
    kalanlar -= 1



# print("ANS -->>",ans[1:])
print(*ans[1:])

def ansCheck(sumArray,answer,k):
    for i in range(1,len(sumArray)):
        if sumArray[i]!=sum(answer[i:i+k]):
            print("Hatalıysam ara beni",i,sumArray[i],sum(answer[i:i+k]))
            return False
    return True

print("ANSCHECK",ansCheck(S,ans,k))


"""

-bas
10 8 3
3 4 7 9 12 16 21 27
5 4
9 8

-son
10 8 3
3 4 7 9 12 16 21 27
5 4
7 5

-orta
10 8 3
3 4 7 9 12 16 21 27
7 5
9 8

----1 1 1 2 4 3 5 8 8 11

10 9 2
863 337 734 375 368 605 447 487 87
2 835

---28 835 -498 1232 -857 1225 -620 1067 -580 667



100 84 17
301 939 872 392 106 525 543 423 693 116 609 34 203 429 360 307 914 19 654 808 431 537 208 376 191 582 900 151 304 800 796 894 311 664 615 844 589 338 177 938 239 204 484 496 62 860 670 54 854 164 770 265 143 975 565 219 541 624 740 647 897 750 669 433 808 333 876 35 398 606 508 645 193 719 571 103 344 194 716 611 183 936 279 204
12 945
82 20
2 263
24 466
49 369
88 733
23 552
44 285
9 201
76 746
64 272
73 215
96 276
21 504
51 225
86 628

-----960 263 2114 790 -958 534 586 -102 201 541 86 945 666 -334 1005 -6245 1169 -322 196 1634 504 -539 552 466 168 -376 1034 -489 1114 892 -403 952 -5638 274 313 350 1257 610 -868 720 281 559 -58 285 -336 1610 888 -305 369 -5285 225 542 95 1006 449 -107 21 246 839 -46 -149 462 1420 272 495 -321 -4679 -280 420 927 596 103 215 104 362 746 204 -296 381 1184 647 20 222 -5520 83 628 829 733 -349 741 -44 -106 987 54 226 276 756 1400 -637 147
"""