def fuchsia_sort(n, k, sums, known_nums):
    ans = [None] * n
    for i in range(k - 1):
        ans[known_nums[i][0] - 1] = known_nums[i][1]
        for j in range(known_nums[i][0] - 1 + k, n, k):
            ans[j] = ans[j - k] + (sums[j - k + 1] - sums[j - k])
        for j in range(known_nums[i][0] - 1 - k, -1, -k):
            ans[j] = ans[j + k] - (sums[j + 1] - sums[j])
    
    missing_idx = -1
    for i in range(k):
        if ans[i] == None:
            missing_idx = i
            ans[missing_idx] = 0
            break
    ans[missing_idx] = sums[0] - sum(ans[: k])
    for j in range(missing_idx + k, n, k):
        ans[j] = ans[j - k] + (sums[j - k + 1] - sums[j - k])

    return ans

n, m, k = list(map(int, input().split()))
sums = list(map(int, input().split()))

known_nums = []
for _ in range(k - 1):
    ind, num = list(map(int, input().split()))
    known_nums.append((ind, num))
    
print(*fuchsia_sort(n, k, sums, known_nums))