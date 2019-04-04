

n=int(input().strip())
arr=list(map(int,input().strip().split()))

srt=sorted(arr,reverse=True)
# print(arr,"\n",srt)

ans=0
rus=1
while arr:
    if(srt[0]==arr[0]):
        srt.pop(0)
        arr.pop(0)
        ans+=rus
        rus=1
    else:
        arr.append(arr.pop(0))
        rus+=1

print(ans)
