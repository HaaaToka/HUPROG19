
import os
from time import time
a=time()

inputs = os.listdir("./input")
for inp in inputs:
    inputfile = open("input/" + inp, "r")
    number = inp[5:7]
    out = open("output/output" + number + ".txt", "w")
    print("su an " + number + " nolu outputu hazirliyorum... gecen sure: " + str(time() - a))

    N=int(inputfile.readline())

    kazanan = {"K": 0, "A": 0}

    for _ in range(N):
        temp = inputfile.readline().strip().split()
        b, m = map(int, temp[0:2])
        if (b - 1) % (m + 1) != 0:
            kazanan[temp[2]] += 1
        else:
            if temp[2] == "K":
                kazanan["A"] += 1
            else:
                kazanan["K"] += 1

    if (kazanan["K"] < kazanan["A"]):
        print("Kayra",kazanan["K"],file=out)
    elif (kazanan["K"] > kazanan["A"]):
        print("Asya",kazanan["A"],file=out)
    else:
        print("AAAAAAAAAAAAAAAAAAAAAA")
