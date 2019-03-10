

class Node:
    def __init__(self,char):
        self.branch = []
        self.next_node = []
        self.count = 0
        self.char = char
        self.center_all = 0

class Root:
    def __init__(self):
        self.head = Node("")

    def new_node(self,entry):
        for x in range(len(entry)+1):
            for y in range(x,-1,-1):
                self.temp = self.head
                for z in range(y,x):
                    if entry[z] in self.head.branch:
                        dex = self.head.branch.index(entry[z])
                        self.head = self.head.next_node[dex]
                    else:
                        self.head.branch.append(entry[z])
                        self.head.next_node.append(Node(entry[y:x]))
                        self.head = self.head.next_node[self.head.branch.index(entry[z])]
                self.head.count += 1
                #index 0 dan basliyor
                self.head.center_all += (y+(x-y)//2)#find center of word
                self.head = self.temp

    def whole_words(self,current):
        for word in current.next_node:
            self.whole_words(word)

        if current != self.head:
            center = current.center_all#/current.count
            if center in dic:
                dic[center].append(current.count)
            else:
                dic[center] = [current.count]

from operator import itemgetter


dic = {}
n = int(input())
boo = input()


a = Root()
a.new_node(boo)
a.whole_words(a.head)
output = []
dic = {x:y for x,y in sorted(dic.items(), key=itemgetter(0), reverse=True)}
last = -1
for y in dic.values():
    arr = sorted(list(set(y)), reverse=True)
    if arr[0] == last:
        output.extend(arr[1:])
    else:
        output.extend(arr)
    last = arr[-1]


print("".join(map(str,output)))


