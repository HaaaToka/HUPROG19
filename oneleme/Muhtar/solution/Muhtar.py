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


frst = list(map(int, input().split()))
frst_degree = list(map(int, input().split()))
scnd = list(map(int, input().split()))
scnd_degree = list(map(int, input().split()))
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
print(median)
if count >= len(answer)//2:
    print("EVET")
else:
    print("HAYIR")


