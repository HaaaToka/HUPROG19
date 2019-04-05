from collections import defaultdict

class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph  = defaultdict(list) 
  
    def addEdge(self, v, w):  
        self.graph[v].append(w)  
        self.graph[w].append(v)  
  
    def isCyclicUtil(self, v, visited, parent): 
        visited[v] = True
  
        for i in self.graph[v]: 
            if visited[i] == False: 
                if self.isCyclicUtil(i, visited, v) == True: 
                    return True
            elif i != parent: 
                return True
  
        return False

    def isTree(self): 
     
        visited = [False] * self.V
   
        if self.isCyclicUtil(0, visited, -1) == True: 
            return False

        for i in range(self.V): 
            if visited[i] == False: 
                return False
  
        return True


class Input():

    def __init__(self, N, y, k, S, A, B, F, D):
        self.N = N
        self.y = y
        self.k = k
        self.S = S
        self.A = A
        self.B = B
        self.F = F
        self.D = D

    def check_constraints(self):
        if not (1 <= self.N <= 2 * 10**5 and 1 <= self.S <= 2 * 10**5 and 1 <= self.k <= 10**7):
            return False

        for i in range(self.S):
            if not (1 <= self.A[i] <= self.N and 1 <= self.B[i] <= self.N and 1 <= self.F[i] <= 10**5 and -10**3 <= self.D[i] <= 10**3): 
                return False

        return True


    def is_there_negative(self):
        is_there_neg = False
        for num in self.D:
            if num < 0:
                is_there_neg = True
        return is_there_neg

    

def assert_tree(graphs):
    for graph in graphs:
        if not graph.isTree():
            print("Assert Tree: FAILED!")
            return
    print("Assert Tree: OK...")


def assert_constraints(inputs):
    for inp in inputs:
        if not inp.check_constraints():
            print("Assert Constraints: FAILED!")
            return
    print("Assert Constraints: OK...")


def assert_negative_gain(inputs):
    for inp in inputs:
        if not inp.is_there_negative():
            print("Assert Negatives: FAILED!")
            return
    print("Assert Negatives: OK...")


inputs = []
graphs = []
for i in range(20):
    fin = open("input/input" + str(i).zfill(2) + ".txt", "r")
    n, y, k = list(map(int, fin.readline().split()))
    graph = Graph(n)
    for _ in range(n - 1):
        u, v = list(map(int, fin.readline().split()))
        graph.addEdge(u - 1, v - 1)

    s = int(fin.readline())
    A = []
    B = []
    F = []
    D = []
    for _ in range(s):
        a, b, f, d = list(map(int, fin.readline().split()))
        A.append(a)
        B.append(b)
        F.append(f)
        D.append(d)

    inputs.append(Input(n, y, k, s, A, B, F, D))
    graphs.append(graph)


assert_tree(graphs)
assert_constraints(inputs)
assert_negative_gain(inputs)

