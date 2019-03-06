

n, m, k, p, x = map(int, input().split())
pcs = []
for _ in range(n):
    pcs.append(list(map(int, input().split())))


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

print(fp_min_index + 1)
