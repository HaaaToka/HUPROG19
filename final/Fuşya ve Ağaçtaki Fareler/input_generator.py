import random as rd

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


n = [100] * 5 + [1000] * 5 + [10000] * 5 + [2*10 ** 5] * 5
s = [100] * 5 + [1000] * 5 + [10000] * 5 + [2*10 ** 5] * 5
q = [1]*20 #[10] * 15 + [2] * 5

# Fuschia start points
y = [rd.randint(1, 100) for i in range(5)] + [rd.randint(1, 1000) for i in range(5)] + [rd.randint(1, 10000) for i in range(5)] + [rd.randint(1, 10 ** 5) for i in range(5)]    
# Fuschia starting paw powers
p = [rd.randint(10, 10 ** 7) for i in range(20)]

#Generate inputs
for i in range (16,20):
    print(i," input hazirlaniyor",q[i],n[i],y[i],p[i])
    fout = open("input/input" + str(i).zfill(2) + ".txt", "w")
    # print(q[i], file=fout)
    n_m_queries = [n[i] for x in range(q[i])]
    for j in range(q[i]):
        print(n_m_queries[j], y[i], p[i], file=fout)
        edges = generate_random_tree(n_m_queries[j])
        assert(len(edges) == n_m_queries[j] - 1)
        for edge in edges:
            print(edge[0], edge[1], file=fout)

        print(n_m_queries[j], file=fout)
        for _ in range(n_m_queries[j]):
            pair = get_random_pair(n_m_queries[j])
            print(pair[0], pair[1], rd.randint(1, 10 ** 5), rd.randint(-10**2, 10 ** 3), file=fout)
