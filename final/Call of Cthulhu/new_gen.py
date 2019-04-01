from collections import defaultdict
from operator import itemgetter
import time
import random

nums= [10]*3+[200]*2+[500]*3+[600]*1+[700]*1+[800]*5+[1000]*15
def solve(n, word):
    n = n
    word = word
    start = time.time()
    values = dict()
    for i in range(len(word)):
           for j in range(i, len(word)):
                  if word[i:j+1] not in values:
                         values[word[i:j+1]] = [i+((j)-i)//2, 1]
                  else:
                         weight, rec = values[word[i:j+1]]
                         values[word[i:j+1]] = [weight+i+((j)-i)//2, rec+1]
                  

    final = defaultdict(set)
    output = []
    for both in sorted(values.values(),
                    key=itemgetter(0),reverse=True):
           final[both[0]].add(both[1])
    last = -1
    for y in final.values():
        arr = sorted(list(set(y)), reverse=True)
        if arr[0] == last:
            output.extend(arr[1:])
        else:
            output.extend(arr)
        last = arr[-1]

    print("time:",time.time()-start)
    return "".join(map(str,output))

location = "C:/Users/onurf/Desktop/Q/Cthulhu/test cases/"
for i,num in enumerate(nums):
    with open(location+"input/input"+str(i).zfill(2)+".txt","w") as inputFile:
        with open(location+"output/output"+str(i).zfill(2)+".txt","w") as outputFile:
            print("Test case", i, "Started", num)
            word = "".join([chr(random.randint(97,122)) for _ in range(num)])
            inputFile.write(str(num))
            inputFile.write("\n"+word)
            result = solve(num, word)

            outputFile.write(result)
            print("Test case", i, "Done")
