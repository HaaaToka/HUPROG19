import random
n,k,r1,c1,r2,c2 = list(map(int,input().split()))
lis = [".","x","x"]
f = open("in.txt","w")
f.write(str(n)+" "+str(k)+" "+str(r1)+" "+str(c1)+" "+str(r2)+" "+str(c2)+"\n")
for i in range(n):
    for e in range(n):
        f.write(lis[random.randint(0,1)])
    f.write("\n")
f.close()
