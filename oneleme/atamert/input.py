from random import randint
from time import time
a=time()

testcase=1

maxL=(10**2)

for i in range(0,testcase):
    print("input ",i," gecen sure", time()-a)
    if i<10:
        out= open("input/input0"+str(i)+".txt","w")
    else:
        out = open("input/input"+str(i)+".txt","w")

    N = randint(10**5,(10**6))
    print(N,file=out)

    x,y=0,0
    ll=[]
    while N>len(ll):
        nameL,surnameL=randint(1,maxL),randint(1,maxL)
        name,surname="",""
        for __ in range(nameL):
            t=randint(97,122)
            x+=t
            name+=chr(t)
        for __ in range(surnameL):
            t=randint(97,122)
            y+=t
            surname+=chr(t)
        #if [x,y] in ll:
        #    continue
        ll.append([x,y])
        print(name,surname,file=out)

    out.close()