n, m, k = list(map(int, input().split()))
sums = list(map(int, input().split()))
final_result = ["?"]*n
given = {}
for _ in range(k-1):
    idx, val = list(map(int, input().split()))
    given[idx-1] = val
    final_result[idx-1] = val
#print(final_result)
for idx, val in given.items():
    # şuanki indexten k kadar çıkar
    # index - k toplam değerde, 1 eksiği akdar olucak
    # indexi k kadar azalt
    #yeni yeri bul
    idx_now = idx
    which = (idx_now) - k + 1
    cur_val = val
    #print(which)
    while idx_now > k:
        final_result[idx_now - k] = cur_val - (sums[which] - sums[which - 1])
        cur_val = final_result[idx_now - k]
        idx_now -= k
        which = (idx_now) - k + 1

    #print(final_result)

    idx_now = idx
    which = (idx_now)
    cur_val = val
    while idx_now < n-k:
        final_result[idx_now + k] = cur_val - (sums[which] - sums[which + 1])
        cur_val = final_result[idx_now + k]
        idx_now += k
        which = idx_now

    #print(final_result)
for x in range(0,n-k+1):
    current = final_result[x: x + k]
    total = 0
    idx = -1
    for i, val in enumerate(current):
        if val != "?":
            total += val
        else:
            idx = i
    if idx != -1:
        final_result[x+idx] = sums[x] - total

print(*final_result)