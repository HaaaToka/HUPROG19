from collections import deque
import heapq

n = int(input())
customer_money = list(map(int, input().split()))
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
print(bribe)
