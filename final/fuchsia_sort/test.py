
def assert_non_zero():
    for i in range(30):
        fin = open("input/input" + str(i).zfill(2) + ".txt", "r")
        n, k = list(map(int, fin.readline().split()))
        arr = list(map(int, fin.readline().split()))
        if n == 0 or k == 0:
            return "Failed, n or k contains 0 in input " + str(i)
        for num in arr:
            if num == 0 : return "Failed, sum array contains 0 in input " + str(i)
        for j in range(k - 1):
            known_num = list(map(int, fin.readline().split()))
            if len(known_num) != 2:
                return "There is more than 2 numbers in known index in input " + str(i)
            if known_num[0] == 0 or known_num[1] == 0:
                return "Known index contains 0 element in input " + str(i)
    return "OK"
            
"""
for i in range(30):
    fin = open("input/input" + str(i).zfill(2) + ".txt", "r")
    n, k = list(map(int, fin.readline().split()))
    arr = list(map(int, fin.readline().split()))
    print(str(i) + " : " + str(len(arr)))
    """

from fuschias_array import fuchsia_sort

fin = open("input31.txt" , "r")
fout = open("my_out.txt", "w")
n, m, k = list(map(int, fin.readline().split()))
sums = list(map(int, fin.readline().split()))

known_nums = []
for _ in range(k - 1):
    ind, num = list(map(int, fin.readline().split()))
    known_nums.append((ind, num))
    
print(*fuchsia_sort(n, k, sums, known_nums), file=fout)
