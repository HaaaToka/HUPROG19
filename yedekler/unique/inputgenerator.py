import random as rd

"""

5<=N<=10^5 <br>
1<=Q<=10^5 <br>
1<=A_i<10^3 <br>
1<=x<10^2 (arttırma miktarı yada esitleme) <br>


"""

testcase=1

for i in range(testcase):
    print(i,". input oluşturuluyor...")

    with open("./input/input"+str(i).zfill(2)+".txt","w") as inputFile:

        n,q=0,0
        if 0<=i<5:
            n=rd.randint(5,10)
            q=rd.randint(5,10)
            print(n,q,file=inputFile)
            print(n,q)
            for i in range(n):
                print(rd.randint(1,10**1),end=' ',file=inputFile)
            print(file=inputFile)


        elif 5<=i<10:
            n=rd.randint(10**2,10**3)
            q=rd.randint(10**2,10**3)
            print(n,q,file=inputFile)
            print(n,q)
            for i in range(n):
                print(rd.randint(1,10**2),end=' ',file=inputFile)
            print(file=inputFile)


        elif 10<=i<15:
            n=rd.randint(10**3,10**4)
            q=rd.randint(10**3,10**4)
            print(n,q,file=inputFile)
            print(n,q)
            for i in range(n):
                print(rd.randint(1,5*10**2),end=' ',file=inputFile)
            print(file=inputFile)


        elif 15<=i<20:
            n=rd.randint(10**4,10**5)
            q=rd.randint(10**4,10**5)
            print(n,q,file=inputFile)
            for i in range(n):
                print(rd.randint(1,10**3),end=' ',file=inputFile)
            print(file=inputFile)




        l=rd.randint(1,n)
        r=rd.randint(l,n)
        quu=[]
        quu.append(["F",l,r])
        quu.append(["U",l,r,rd.randint(1,100)])
        quu.append(["S",l,r,rd.randint(1,100)])
        for _ in range(q-3):
            sans=rd.randint(1,10)
            l=rd.randint(1,n)
            r=rd.randint(l,n)
            if sans==1:
                #print("U",l,r,rd.randint(1,100),file=inputFile)
                quu.append(["U",l,r,rd.randint(1,100)])
            if sans==2:
                #print("S",l,r,file=inputFile)
                quu.append(["S",l,r,rd.randint(1,100)])
            else:
                #print("F",l,r,file=inputFile)
                quu.append(["F",l,r])
        rd.shuffle(quu)
        for elem in quu:
            print(*elem,file=inputFile)
