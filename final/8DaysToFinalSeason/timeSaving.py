import random
lis = [5,5,5,10,20,20,20,50,50,50,100,100,1000,1000,10000,50000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000]
lis = lis+[100000,100000]*5
for i in range(len(lis)):
    with open("./input/input"+str(i).zfill(2)+".txt","w") as inputFile:
        for _ in range(5):
            n = random.randint(2,lis[i])
            m = random.randint(2,lis[i])
            c = random.randint(0,min(200,n*m-2))
            d = random.randint(0,c)
            mod = random.randint(10,10**9+7)
            print(n,m,c,d,mod,file = inputFile)
            s = set()
            while len(s) < c:
                a = random.randint(1,n)
                b = random.randint(1,m)
                if (a == 1 and b == 1) or (a == n and b==m):
                    continue
                s.add((a,b))
            for e in s:
                print(e[0],e[1],file = inputFile)
                
