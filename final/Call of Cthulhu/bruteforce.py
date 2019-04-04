from collections import defaultdict
from math import ceil,floor
from operator import itemgetter

n=int(input().strip())
txt="<"
txt+=input().strip()

def tp():
    return [0,0]

AB=defaultdict(tp)

for i in range(1,n+1):
    temp=""+txt[i]
    AB[temp][1]+=1
    AB[temp][0]+=i+floor((i-i)/2)
    for k in range(i+1,n+1):
        temp+=txt[k]
        AB[temp][1] += 1
        AB[temp][0] += i + floor((k - i) / 2)


srt=sorted(AB.values(),key=itemgetter(0,1))

zp=str(srt[0][1])
cur=srt[0][1]
for key,value in srt[1:]:
    if cur!=value:
        zp+=str(value)
        cur=value
print(zp)
