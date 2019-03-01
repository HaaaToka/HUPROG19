from random import randint
from time import time
a=time()

testcase=20

for i in range(testcase):
    print("input ",i," gecen sure", time()-a)
    if i<10:
        out= open("input/input0"+str(i)+".txt","w")
    else:
        out = open("input/input"+str(i)+".txt","w")

    N = randint(10,10**2 -1)
    if N % 2==0:
        N-=1

    print(N,file=out)
    for k in range(N):
        B = randint(10, 10 ** 9 - 1)
        M = randint(1, B-1)
        who=randint(0,1)
        if who:
            print(B,M,"K",file=out)
        else:
            print(B, M, "A", file=out)

    out.close()
