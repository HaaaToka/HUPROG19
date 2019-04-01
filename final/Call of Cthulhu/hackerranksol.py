from collections import defaultdict
n = int(input())
word = input()

values = dict()
for i in range(len(word)):
        for j in range(i, len(word)):

            if word[i:j+1] not in values:
                 values[word[i:j+1]] = [i+((j)-i)//2, 1]
            else:
                weight, rec = values[word[i:j+1]]
                values[word[i:j+1]] = [weight+i+((j)-i)//2, rec+1]
              
final = defaultdict(set)
output = []
for both in sorted(values.values(),
                key=lambda x: x[0],reverse=True):
       final[both[0]].add(both[1])
values = []
word = ""
last = -1
for y in final.values():
    arr = sorted(list(set(y)), reverse=True)
    #print(last,arr)
    if arr[0] == last:
        output.extend(arr[1:])
    else:
        output.extend(arr)
    last = arr[-1]

##print(final)
print("".join(map(str,output)))
