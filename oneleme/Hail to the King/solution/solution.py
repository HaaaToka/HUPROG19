import sys
FILEDIR = ""
sys.stdin = open(FILENDIR)

*_,k = list(map(int, input().split()))

frst = list(map(int, input().split()))
frst_degree = list(map(int, input().split()))
scnd = list(map(int, input().split()))
scnd_degree = list(map(int, input().split()))


total = []
for (n, d) in zip(frst, frst_degree):
    total.append((n * 7 + d * 3, 0))

for (n, d) in zip(scnd, scnd_degree):
    total.append((n * 7 + d * 3, 1))



std = k


start = time.time()
total.sort(key=lambda x: x[0])


if len(total) % 2 == 0:
    median = (total[len(total) // 2 - 1][0], total[(len(total) // 2)][0])
else:
    median = total[len(total) // 2][0]

if type(median) != tuple:

    answer = total[binary_search_lower(median - std, total):binary_search_upper(median + std, total)]
    count = 0
    for i in answer:
        if i[1] == 0:
            count += 1
    print(str(median))
    print(str(count))
else:
    # print(median)
    left_boundary = median[0] - k
    right_boundary = median[1] + k
    l_idx = 0
    r_idx = 0
    flag = True
    for i in range(len(total)):
        if right_boundary >= total[i][0] >= left_boundary:
            r_idx = i
            if flag:
                l_idx = i
                flag = False
            if median[0] + k >= total[i][0] >= left_boundary:
                ref_r = i+1

    ref_l = l_idx
    ref_c = 0
    ref_med = median[0]
    for i in range(ref_l, ref_r + 1):
        if ref_med + k >= total[i][0] >= ref_med - k:
            if total[i][1] == 0:
                ref_c += 1
        else:
            break
    max_c = ref_c
    right_flag = False
    left_flag = False
    if median[0] != median[1]:
        for num in range(median[0], median[1] + 1):

            cur_r = num + k
            cur_l = num - k
            while not (cur_r >= total[ref_l][0] >= cur_l):
                if total[ref_l][1] == 0:
                    ref_c -= 1
                ref_l += 1
                if ref_l > r_idx:
                    left_flag = True
                    break
            while (cur_r >= total[ref_r][0] >= cur_l):
                if total[ref_r][1] == 0:
                    ref_c += 1
                ref_r += 1
                if ref_r > r_idx:
                    right_flag = True
                    break

            if ref_c > max_c:
                max_c = ref_c
                ref_med = num
            if right_flag:
                break
            if left_flag:
                break

    print(ref_med)
    print(max_c)






#10.400695562362671
