import random
a = input()
b = int(input())
d = 10
lis = ["---","- -","-- "," --"," - "]
fl = open("input/input"+a+".txt","w")
fl.write(str(d)+"\n")
for e in range(d):
    fl.write(str(b)+"\n")
    for i in range(b):
        fl.write(lis[random.randint(0,4)]+"\n")
fl.close()
