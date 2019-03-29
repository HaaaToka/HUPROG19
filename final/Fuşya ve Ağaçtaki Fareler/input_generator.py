import random as rd

n = [100] * 5 + [1000] * 5 + [10000] * 5 + [10 ** 5] * 5
s = [10] * 5 + [100] * 5 + [1000] * 5 + [10000] * 5

def generate_random_tree(n):
    seen = set()
    edges = []
    u = rd.randint(1, n)
    seen.add(u)
    nums = set([x for x in range(1, n + 1) if x != u])
    for _ in range(n - 1):
        v = rd.sample(nums, 1)[0]
        edges.append((u, v))
        nums.remove(v)
        seen.add(v)
        u = rd.sample(seen, 1)[0]
    return edges

def get_random_pair(n):
    a = rd.randint(1, n)
    b = rd.randint(1, n)
    while b == a:
        b = rd.randint(1, n)
    return (a, b)

# Fuschia start points
y = [rd.randint(1, 100) for i in range(5)] + [rd.randint(1, 1000) for i in range(5)] + [rd.randint(1, 10000) for i in range(5)] + [rd.randint(1, 10 ** 5) for i in range(5)]    
# Fuschia starting paw powers
p = [rd.randint(1, 10 ** 7) for i in range(20)]
print(generate_random_tree(10))
#Generate inputs
"""
for i in range (20):
    fout = open("input/input" + str(i).zfill(2) + ".txt", "w")
    print(n[i], y[i], p[i], file=fout)
    edges = generate_random_tree(n[i])
    assert(len(edges) == n[i] - 1)
    for edge in edges:
        print(edge[0], edge[1], file=fout)

    print(s[i], file=fout)
    for _ in range(s[i]):
        pair = get_random_pair(n[i])
        print(pair[0], pair[1], rd.randint(1, 10 ** 7), rd.randint(1, 10 ** 7), file=fout)
        """
    
    
    
