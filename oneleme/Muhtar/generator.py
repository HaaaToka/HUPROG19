import random

def binary_search(find, arr):

    f = find
    u = len(arr)-1
    d = 0
    while u >= d:
        mid = d+(u-d)//2
        if  arr[mid][0] > f:
            u = mid-1
        elif arr[mid][0] < f:
            d = mid +1
        else:
            break
    return d+(u-d)//2

num = 10**5
#Denenler 3 x 10**2
# 2 x 10**3
# 2 x 10**4
# 4 x 10**5
location = "C:/Users/onurf/Desktop/Q/Muhtar/test cases/"
last = 7
for k in range(last,last+4):
    with open(location+"input0{}.txt".format(k),"w") as inputFile:
        with open(location+"output0{}.txt".format(k),"w") as outputFile:
            frst = [random.randint(0,10**6) for _ in range(num)]
            frst_degree = [random.randint(0,10**6) for _ in range(num)]
            scnd = [random.randint(0,10**6) for _ in range(num)]
            scnd_degree = [random.randint(0,10**6) for _ in range(num)]
            inputFile.write(str(num))
            inputFile.write("\n"+" ".join(map(str, frst)))
            inputFile.write("\n"+" ".join(map(str, frst_degree)))
            inputFile.write("\n"+" ".join(map(str, scnd)))
            inputFile.write("\n"+" ".join(map(str, scnd_degree)))
            total = []
            sum = 0
            for (n, d) in zip(frst, frst_degree):
                total.append((n*d,0))
                sum += n*d

            for (n, d) in zip(scnd, scnd_degree):
                total.append((n*d,1))
                sum += n*d

            var = 0
            mean = sum//len(total)
            for i in total:
                var += (i[0]-mean)**2
            std = (var/len(total))**(1/2)
            total.sort()
            if len(total)%2 == 0:
                median = (total[len(total)//2][0]+total[(len(total)//2)-1][0])/2
            else:
                median = total[len(total)//2][0]

            answer = total[binary_search(median+std, total):binary_search(median-std, total)]
            count = 0
            for i in answer:
                if i[1] == 0:
                    count += 1
            outputFile.write(str(median))
            if count >= len(answer)//2:
                outputFile.write("\nEVET")
            else:
                outputFile.write("\nHAYIR")


