import random as rd
from fuschia_sort_sol import fuchsia_sort


def prng(n, exclude):
    choices = [x for x in range(1, n + 1) if x not in exclude]
    return rd.choice(choices)

input_sizes = [10, 100, 100, 100, 100, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 10**4, 10**4, 10**4, 10**4, 10**4, 10**4, 10**4, 10**4, 10**4, 10**5, 10**5, 10**5, 10**6, 10**6]
k_sizes = [2, 17, 13, 14, 8, 56, 72, 99, 101, 342, 672, 240, 120, 78, 92, 133, 242, 562, 427, 356, 840, 257, 356, 216, 271, 302, 999, 666, 621, 987]
for i in range(30):
    fin = open("input" + str(i).zfill(2) + ".txt", "w")
    fout = open("output" + str(i).zfill(2) + ".txt", "w")
    k = k_sizes[i]
    n = input_sizes[i]
    len_of_sums = n - k + 1
    sums = [rd.randint(k, 1000) for _ in range(len_of_sums)]
    print(n, k, file=fin)
    print(*sums, file=fin)
    chosen = set()
    known_nums = []
    for _ in range(k - 1):
        choice = prng(n, chosen)
        ind = (choice - 1) % k
        for j in range(ind, n, k):
            chosen.add(j + 1)
        for j in range (ind, -1, -k):
            chosen.add(j + 1)
        number = rd.randint(k, 1000)
        if _ == k - 2:
            print(choice, number, file=fin, end="")
        else:
            print(choice, number, file=fin)
        known_nums.append((choice, number))
    out_arr = fuchsia_sort(n, k, sums, known_nums)
    print(*out_arr, sep=" ", file=fout)

            

"""

k=2 n=5 
1 2 3 4 5 s = 4
k=3 n=5
1 2 3 4 5 s = 3
k=4 n=5
1 2 3 4 5 s = 2

k=2 n=7
1 2 3 4 5 6 7 s = 6
k=3 n=7
1 2 3 4 5 6 7 s = 5


"""
    

