from random import randint
from time import time
a=time()

testcase=10

maxL=10**5

for i in range(testcase):
    print("input ",i," gecen sure", time()-a)
    if i<10:
        out= open("input/input0"+str(i)+".txt","w")
    else:
        out = open("input/input"+str(i)+".txt","w")

    N = randint(10,10**1)
    print(N,file=out)

    for _ in range(N):
        nameL,surnameL=randint(1,maxL),randint(1,maxL)
        name,surname="",""
        for __ in range(nameL):
            name+=chr(randint(97,122))
        for __ in range(surnameL):
            surname+=chr(randint(97,122))
        print(name,surname,file=out)

    out.close()