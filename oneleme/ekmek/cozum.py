
N = int(input())

kazanan = {"K":0,"A":0}

for _ in range(N):
    temp = input().strip().split()
    b,m = map(int,temp[0:2])
    if(b-1)%(m+1)!=0:
        kazanan[temp[2]]+=1
    else:
        if temp[2]=="K":
            kazanan["A"]+=1
        else:
            kazanan["K"]+=1

if(kazanan["K"]<kazanan["A"]):
    print("Kayra",kazanan["K"])
else:
    print("Asya",kazanan["A"])


"""

2
3 2 K
5 1 A


"""
