import random
a = input()
b = int(input())
lis = ["---","- -","-- "," --"," - "]
fl = open(a,"w")
fl.write(str(b)+"\n")
for i in range(b):
    fl.write(lis[random.randint(0,4)]+"\n")
fl.close()
