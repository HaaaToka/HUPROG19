import random
import time


def countSort(arr):
    maxi = max(arr, key = lambda x: x[0])[0]
    mini = min(arr, key= lambda x:x[0])[0]
    bt_range = maxi-mini+1
    count = [0]*bt_range
    output = [0]*len(arr)

    for i in range(len(arr)):
        count[arr[i][0] - mini] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr)-1, -1, -1):
        output[count[arr[i][0]-mini]-1] = arr[i]
        count[arr[i][0] - mini] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

    return arr

def binary_search_upper(find, arr):
    f = find
    u = len(arr)-1
    d = 0
    while u >= d:
        mid = d+(u-d)//2
        if  arr[mid][0] > f:
            u = mid-1
        elif arr[mid][0] <= f:
            d = mid +1
        else:
            break
    return d+abs(u-d)//2

def binary_search(find, arr):
    f = find
    u = len(arr)-1
    d = 0
    while u >= d:
        mid = d+(u-d)//2
        if  arr[mid][0] >= f:
            u = mid-1
        elif arr[mid][0] <f:
            d = mid +1
        else:
            break
    return d+abs(u-d)//2

def binary_search_lower(find, arr):
    f = find
    u = len(arr)-1
    d = 0
    while u >= d:
        mid = d+(u-d)//2
        if  arr[mid][0] >= f:
            u = mid-1
        elif arr[mid][0] <f :
            d = mid +1
        else:
            break
    return d+abs(u-d)//2


nums= [10**3]*6+[10**4]*10+[10**6]*8

location = "C:/Users/onurf/Desktop/Q/Muhtar/test cases/"
RANGE = 100
for i,num in enumerate(nums):
    with open(location+"/input/input"+str(i).zfill(2)+".txt","w") as inputFile:
        with open(location+"output/output"+str(i).zfill(2)+".txt","w") as outputFile:
            print(i," started time is: " , time.ctime())
            N = random.randint((num//4),num)-random.randint(0,1)
            M = num-N-random.randint(0,1)
            frst = [random.randint(1,RANGE) for _ in range(num)]
            frst_degree = [random.randint(1,RANGE) for _ in range(num)]
            scnd = [random.randint(1,RANGE) for _ in range(num)]
            scnd_degree = [random.randint(1,RANGE) for _ in range(num)]


            total = []
            for (n, d) in zip(frst, frst_degree):
                total.append((n * 7 + d * 3, 0))

            for (n, d) in zip(scnd, scnd_degree):
                total.append((n * 7 + d * 3, 1))

            max_differ = max(total, key=lambda x:x[0])[0]
            min_differ = min(total, key=lambda x:x[0])[0]
            k = random.randint(10, (max_differ-min_differ)//2)
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
                count = 0
                for i in answer:
                    if i[1] == 0:
                        count += 1
                outputFile.write(str(median) + "\n")
                outputFile.write(str(count))
            else:
                # print("Total:",total)
                answer = total[binary_search_lower(median[0] - std, total):binary_search_upper(median[1] + std, total)]
                # print("Answer:", answer)
                left_med = binary_search(median[0], answer)
                right_med = binary_search(median[1], answer)
                count = 0
                start = left_med
                min_med = -1
                max_count = -1
                si = 0
                sj = left_med
                sj_r = left_med + 1
                eof = True
                # print("K:", k)
                for i in range(left_med + 1):
                    if answer[i][1] == 0:
                        count += 1
                while answer[left_med][0] + k >= answer[sj_r][0]:
                    if answer[sj_r][1] == 0:
                        count += 1
                    sj_r += 1
                    if sj_r >= len(answer):
                        eof = False
                        break
                max_count = count
                min_med = answer[left_med][0]

                for i in range(left_med, right_med + 1):
                    # print("Now:",i, si, sj, sj_r)
                    while abs(answer[si][0] - answer[sj][0]) > k:
                        if answer[si][1] == 0:
                            count -= 1
                        si += 1
                        if si > len(answer):
                            break
                        # print("Second Now:", i, si, sj, sj_r)
                    if eof:
                        while abs(answer[sj][0] - answer[sj_r][0]) <= k:
                            if answer[sj_r][1] == 0:
                                count += 1
                            sj_r += 1
                            # print("Third Now:", i, si, sj, sj_r)
                            if sj_r >= len(answer):
                                eof = False
                                break

                    if count > max_count:
                        max_count = count
                        min_med = answer[sj][0]
                    sj += 1
                outputFile.write(str(min_med)+"\n")
                outputFile.write(str(max_count))





























