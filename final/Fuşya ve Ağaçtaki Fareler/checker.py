import os
import sys

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def isCyclicUtil(self, v, visited, parent):

        visited[v] = True

        for i in self.graph[v]:

            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, v)):
                    return True

            elif parent != i:
                return True

        return False

    def isCyclic(self):

        visited = [False] * (self.V)

        for i in range(self.V):
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, -1)) == True:
                    return True

        return False

"""

1<=N<=10**5
1<=y<=N
1<=k<=10**9
1<=S<=10**5
1<=u<=N
1<=v<=N
1<=a<=N
1<=b<=N
1<=d<=10**9
1<=f<=10**9

"""


inputs = os.listdir("./input")

for file in inputs:

    inFile = open("./input/"+file,"r")
    print(file)
    q=1

    for _ in range(q):

        N,y,k = map(int,inFile.readline().strip().split())

        if not (1<N<=10**5 or 1<=y<=N or 1<=k<=10**9 ):
            print("1Constraints")

        G=Graph(N)
        for __ in range(N-1):

            u,v = map(int,inFile.readline().strip().split())
            G.addEdge(u-1,v-1)

            if not (1<=u<=N or 1<=v<=N):
                print("2COnstraints")

        if G.isCyclic():
            print("HoHo HO cycle var burda")

        S=int(inFile.readline().strip())
        if not (1<=S<=10**5):
            print("3Constraints")

        for __ in range(S):

            a, b, f, d = map(int, inFile.readline().strip().split())

            if not (1<=a<=N or 1<=b<=N or 1<=d<=10**9 or 1<=f<=10**9):
                print("4COnstraints")

