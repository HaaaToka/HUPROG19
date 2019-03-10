import random
from operator import itemgetter

nums= [10]*3+[200]*10+[300]*3+[400]*8


class Node:
    def __init__(self, char):
        self.branch = []
        self.next_node = []
        self.count = 0
        self.char = char
        self.center_all = 0


class Root:
    def __init__(self):
        self.head = Node("")

    def new_node(self, entry):
        for x in range(len(entry) + 1):
            for y in range(x, -1, -1):
                self.temp = self.head
                for z in range(y, x):
                    if entry[z] in self.head.branch:
                        dex = self.head.branch.index(entry[z])
                        self.head = self.head.next_node[dex]
                    else:
                        self.head.branch.append(entry[z])
                        self.head.next_node.append(Node(entry[y:x]))
                        self.head = self.head.next_node[self.head.branch.index(entry[z])]
                self.head.count += 1
                self.head.center_all += (y + (x - y - 1) // 2)  # find center of word
                self.head = self.temp

    def whole_words(self, current):
        for word in current.next_node:
            self.whole_words(word)

        if current != self.head:
            center = current.center_all  # /current.count
            if center in dic:
                dic[center].append(current.count)
            else:
                dic[center] = [current.count]

location = "C:/Users/onurf/Desktop/Q/Cthulhu/test cases/"
for i,num in enumerate(nums):
    with open(location+"input"+str(i).zfill(2)+".txt","w") as inputFile:
        with open(location+"output"+str(i).zfill(2)+".txt","w") as outputFile:
            print("Test case", i, "Started", num)
            word = "".join([chr(random.randint(97, 122)) for _ in range(num)])
            inputFile.write(str(num))
            inputFile.write("\n"+word)

            dic = {}

            a = Root()
            a.new_node(word)
            a.whole_words(a.head)
            output = []
            dic = {x: y for x, y in sorted(dic.items(), key=itemgetter(0), reverse=True)}
            last = -1
            for y in dic.values():
                arr = sorted(list(set(y)), reverse=True)
                if arr[0] == last:
                    output.extend(arr[1:])
                else:
                    output.extend(arr)
                last = arr[-1]

            outputFile.write("".join(list(map(str, output))))
            print("Test case", i, "Done")


