from collections import defaultdict
from operator import itemgetter
n = int(input())
word = input()

values = dict()
for i in range(len(word)):
        for j in range(i, len(word)):
            
                if word[i:j+1] not in values:
                        values[word[i:j+1]] = [(i+1)+((j)-i)//2, 1]
                else:
                        weight, rec = values[word[i:j+1]]
                        values[word[i:j+1]] = [weight+(i+1)+((j)-i)//2, rec+1]
                print("Başlangıç indeksi:",i+1, ", bitiş indeksi:",j+1,", Formül: {}+floor(({}-{})/2)".format(str(i+1), str(j+1), str(i+1)),", bu tekrardaki alt kelimenin orta değer sonucu:",(i+1)+((j)-i)//2, ", alt kelime:", word[i:j+1],", bu ana kadarki orta değerlerin toplamı:", values[word[i:j+1]][0], "bu ana kadarki tekrar sayısı:",values[word[i:j+1]][1])

print(values)

final = defaultdict(set)
output = []

for both in sorted(values.values(),
                key=itemgetter(0,1)):
       final[both[0]].add(both[1])
print(" ".join(map(lambda x: str(x[1]), sorted(values.values(), key=itemgetter(0,1)))))
values = []
word = ""
last = -1
for y in final.values():
    arr = sorted(list(set(y)))
    #print(last,arr)
    if arr[0] == last:
        output.extend(arr[1:])
    else:
        output.extend(arr)
    last = arr[-1]

##print(final)
print("".join(map(str,output)))
