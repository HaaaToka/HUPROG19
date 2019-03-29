from collections import defaultdict
from math import ceil,floor
from operator import itemgetter

n=int(input().strip())
txt=input().strip()


basbit=defaultdict(int)
tekrar=defaultdict(int)

for i in range(n):
    temp=""+txt[i]
    tekrar[temp]+=1
    basbit[temp]+=i+floor((i-i)/2)
    for k in range(i+1,n):
        temp+=txt[k]
        tekrar[temp] += 1
        basbit[temp]+=i+floor((k-i)/2)

#print(basbit,"\n\n",tekrar)

srt=sorted(basbit.items(),key=itemgetter(1),reverse=True)
#print(srt)

zp=""
for key,value in srt:
    zp+=str(value)
#print(zp)

def zipper(tex):
    ans=""+tex[0]
    cr=tex[0]
    for i in range(1,len(tex)):
        if cr!=tex[i]:
            cr=tex[i]
            ans+=tex[i]
    return ans

print("---------",zipper(zp))
