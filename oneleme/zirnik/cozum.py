

n, m, k, p, x = map(int, input().split())
pcs = []
for _ in range(n):
    pcs.append(list(map(int, input().split())))

fp_min = float("inf")
fp_min_index = -2
for idx, pc in enumerate(pcs):
    price = pc[0]
    if price > x:
        continue
    minimum = min(pc[1:])

    for i in range(1, len(pc)):

        if abs(pc[i] - minimum) > k:
            pc[i] = minimum + k

    pow_sum = sum(pc) - price
    if pow_sum < p:
        continue

    fp = price / pow_sum
    if fp_min > fp:
        fp_min = fp
        fp_min_index = idx

print(fp_min_index + 1)
