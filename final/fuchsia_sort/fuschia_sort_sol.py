"""n, m = list(map(int, input().split()))
sums = list(map(int, input().split()))

known_nums = []
for _ in range(m - 1):
    ind, num = list(map(int, input().split()))
    known_nums.append((ind, num))"""

def fuchsia_sort(n, m, sums, known_nums):
    seen_arr = [False] * n
    ans_arr = [0] * n
    for i in range(m - 1):
        curr_ind_left = known_nums[i][0]
        curr_num_left = known_nums[i][1]
        curr_ind_right = known_nums[i][0]
        curr_num_right = known_nums[i][1]
        ans_arr[curr_ind_left - 1] = curr_num_left
        seen_arr[curr_ind_left - 1] = True

        while curr_ind_left - m >= 1:
            curr_ind_left -= m
            curr_num_left -= sums[curr_ind_left] - sums[curr_ind_left - 1]
            ans_arr[curr_ind_left - 1] = curr_num_left
            seen_arr[curr_ind_left - 1] = True

        while curr_ind_right + m <= n:
            curr_num_right += sums[curr_ind_right] - sums[curr_ind_right - 1] 
            curr_ind_right += m
            ans_arr[curr_ind_right - 1] = curr_num_right
            seen_arr[curr_ind_right - 1] = True


    ind = -1
    for i in range(m):
        if not seen_arr[i]:
            ind = i + 1

    assert(ind != -1)

    

    curr_num = sums[0] - sum(ans_arr[0 : m])
    ans_arr[ind - 1] = curr_num 
    #print("anan : " + str(sum(ans_arr[0:m])))
    #print(curr_num)

    while ind + m <= n:
        curr_num += sums[ind] - sums[ind - 1]
        ind += m
        ans_arr[ind - 1] = curr_num
        

    return ans_arr

#arr = fuchsia_sort(n, m, sums, known_nums)
#print(sum(arr[0:m]))