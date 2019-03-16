import random
import time



nums = [10**3]*6+[10**4]*10+[10**6]*10
location =""
RANGE = 10**6
idx = 0
while idx < len(nums):
    num = nums[idx]
    with open(location+"/input/input"+str(idx).zfill(2)+".txt","w") as inputFile:
        with open(location+"/output/output"+str(idx).zfill(2)+".txt","w") as outputFile:
            print(idx," started time is: " , time.ctime())
            if idx < 18:
                N = random.randint((num//4),num)-random.randint(0,1)#num
                M = random.randint((num//4),num)-random.randint(0,1)#num
                frst = [random.randint(1,RANGE) for _ in range(N)]
                frst_degree = [random.randint(1,RANGE) for _ in range(N)]
                scnd = [random.randint(1,RANGE) for _ in range(M)]
                scnd_degree = [random.randint(1,RANGE) for _ in range(M)]
            else:
                N = num#num
                M = N#num
                frst = []
                frst_degree = []
                scnd = []
                scnd_degree = []
                for i in range(N):
                    which_one = random.randint(0,1)
                    number_append = random.randint(RANGE-1000,RANGE)
                    if which_one == 1:
                        frst.append(number_append)
                        frst_degree.append(number_append)
                    else:
                        scnd.append(number_append)
                        scnd_degree.append(number_append)
                    which_one = random.randint(0,1)
                    number_append = random.randint(1,1)
                    if which_one == 1:
                        frst.append(number_append)
                        frst_degree.append(number_append)
                    else:
                        scnd.append(number_append)
                        scnd_degree.append(number_append)


            total = []
            for (n, d) in zip(frst, frst_degree):
                total.append((n * 7 + d * 3, 0))

            for (n, d) in zip(scnd, scnd_degree):
                total.append((n * 7 + d * 3, 1))




            max_differ = max(total, key=lambda x:x[0])[0]
            min_differ = min(total, key=lambda x:x[0])[0]

            k = random.randint((max_differ-min_differ)//100, (max_differ-min_differ)//4)
            print(N,M)
            print(len(frst), len(scnd))
            print(max_differ, min_differ , k)
            inputFile.write(str(N)+" "+str(M)+" "+str(k))
            inputFile.write("\n"+" ".join(map(str, frst)))
            inputFile.write("\n"+" ".join(map(str, frst_degree)))
            inputFile.write("\n"+" ".join(map(str, scnd)))
            inputFile.write("\n"+" ".join(map(str, scnd_degree)))

            std = k
            total = countSort(total)

            if len(total) % 2 == 0:
                median = (total[len(total) // 2 - 1][0], total[(len(total) // 2)][0])
            else:
                median = total[len(total) // 2][0]

            if type(median) != tuple:

                answer = total[binary_search_lower(median - std, total):binary_search_upper(median + std, total)]
                max_c = 0
                for i in answer:
                    if i[1] == 0:
                        max_c += 1
                outputFile.write(str(median) + "\n")
                outputFile.write(str(max_c))
            else:
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
                            ref_r = i + 1

                ref_l = l_idx
                ref_c = 0
                ref_med = median[0]
                # print(total)
                # print(ref_l, ref_r, "This")
                # print(l_idx, r_idx)
                # count first array
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
                            # print(ref_l, len(total))
                            if total[ref_l][1] == 0:
                                ref_c -= 1
                            ref_l += 1
                            if ref_l > r_idx:
                                left_flag = True
                                break
                        while (cur_r >= total[ref_r][0] >= cur_l):
                            # print(ref_r , len(total))
                            if total[ref_r][1] == 0:
                                # print(total[ref_r])
                                ref_c += 1
                            ref_r += 1
                            if ref_r > r_idx:
                                right_flag = True
                                break

                        if ref_c > max_c:
                            max_c = ref_c
                            ref_med = num
                        if right_flag or left_flag:
                            break

                outputFile.write(str(ref_med)+"\n")
                outputFile.write(str(max_c))
    if max_c != 0:
        idx += 1



















#10.974925756454468










