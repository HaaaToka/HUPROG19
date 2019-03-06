import random as rd

"""

1<=N<=10^3 <br>
1<=M<=10^3 <br>
1<=M_i<10^2 <br>
1<=K<=10^2 <br>
1<=P<=10^3 <br>
1<=X<=10^6 <br>

"""

testcase=20

for i in range(testcase):
    print(i,". input oluşturuluyor...")

    with open("./input/input"+str(i).zfill(2)+".txt","w") as inputFile:

        if 0<=i<5:
            n=rd.randint(1,10)
            m=rd.randint(1,10)
            k=rd.randint(1,3)
            p=rd.randint(1,10)
            x=rd.randint(10**3,10**5)
            print(n,m,k,p,x,file=inputFile)
            for ni in range(n):
                sans=rd.randint(1,10)
                if sans==1:
                    print(rd.randint(x,x+100),file=inputFile,end=' ')
                else:
                    print(rd.randint(100,x),file=inputFile,end=' ')
                for mi in range(m):
                    print(rd.randint(1,10),file=inputFile,end=' ')
                print(file=inputFile)

        elif 5<=i<15:
            n=rd.randint(10,100)
            m=rd.randint(10,100)
            k=rd.randint(10,44)
            p=rd.randint(10,100)
            x=rd.randint(10**4,10**5)
            print(n,m,k,p,x,file=inputFile)
            for ni in range(n):
                sans=rd.randint(1,10)
                if sans==1:
                    print(rd.randint(x,x+100),file=inputFile,end=' ')
                else:
                    print(rd.randint(100,x),file=inputFile,end=' ')
                for mi in range(m):
                    print(rd.randint(10,100),file=inputFile,end=' ')

                print(file=inputFile)
        else:
            n=rd.randint(100,1000)
            m=rd.randint(100,1000)
            k=rd.randint(10,100)
            p=rd.randint(100,1000)
            x=rd.randint(10**5,10**6)
            print(n,m,k,p,x,file=inputFile)
            for ni in range(n):
                sans=rd.randint(1,10)
                if sans==1:
                    print(rd.randint(x,x+100),file=inputFile,end=' ')
                else:
                    print(rd.randint(100,x),file=inputFile,end=' ')
                for mi in range(m):
                    print(rd.randint(1,100),file=inputFile,end=' ')

                print(file=inputFile)
