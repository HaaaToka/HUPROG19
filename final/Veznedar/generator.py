from collections import defaultdict
from operator import itemgetter
import time
import random
from collections import deque
import heapq
	
nums= [100]*2+[1000]*2+[5000]*2+[10000]*5+[50000]*5+[75000]*5+[100000]*15
def solve(n,arr):


	n = n
	customer_money = arr
 
	customers = [ (-1*customer_money[i],-1*i) for i in range(n) ]
	heapq.heapify(customers)
	bribe = 0
	cared = 0
	while customers:
		prev = -1
		new_cared = 0
		current = customers[0]
		while customers and -1*current[1] > prev:
			new_cared += 1
			heapq.heappop(customers)
			temp_prev = -1*current[1]
			while customers and customers[0][0] == current[0] and -1*customers[0][1] > prev:
				current = customers[0]
				heapq.heappop(customers)
				new_cared += 1
			prev = temp_prev
			current = customers[0] if customers else 0
		bribe += n - cared
		cared += new_cared
	return bribe

location = "C:/Users/onurf/Desktop/Q/Veznedar/"
for i,num in enumerate(nums):
    with open(location+"input/input"+str(i).zfill(2)+".txt","w") as inputFile:
        with open(location+"output/output"+str(i).zfill(2)+".txt","w") as outputFile:
            print("Test case", i, "Started", num)
            arr = [random.randint(1,10**5) for _ in range(num)]
            inputFile.write(str(num))
            inputFile.write("\n"+" ".join(map(str,arr)))
            result = solve(num, arr)

            outputFile.write(str(result))
            print("Test case", i, "Done")
