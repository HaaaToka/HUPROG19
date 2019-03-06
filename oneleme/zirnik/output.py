import os
from time import time
a=time()

inputs = os.listdir("./input")
for inp in inputs:

    inputfile = open("input/" + inp, "r")
    number = inp[5:7]
    out = open("output/output" + number + ".txt", "w")
    print("su an " + number + " nolu outputu hazirliyorum... gecen sure: " + str(time() - a))



    n, m, k, p, x = map(int, inputfile.readline().split())
    pcs = []
    for _ in range(n):
        pcs.append(list(map(int, inputfile.readline().split())))


    fp_min = float("inf")
    fp_min_index = -1
    for idx, pc in enumerate(pcs):
        fare = pc[0]

        if fare > x:
            continue

        minimum = min(pc[1:])

        for i in range(1,len(pc)):

            if i + k > minimum:
                pc[i] = minimum+k

        pow_sum = sum(pc) - fare
        if pow_sum < p:
            continue

        fp = fare/pow_sum
        if fp_min > fp:
            fp_min = fp
            fp_min_index = idx

    print(fp_min_index + 1,file=out)
