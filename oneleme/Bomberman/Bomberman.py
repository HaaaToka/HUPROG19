import queue
def check(dp,row,clm,n_row,n_col,arr,que):
    dot_or_x = arr[n_row][n_col]
    root = dp[row][clm]
    nex = dp[n_row][n_col]
    if dot_or_x == "." and (root[0]+1 < nex[0] or root[1] < nex[1]):
        dp[n_row][n_col] = (root[0]+1,root[1])
        que.put((n_row,n_col))
    elif dot_or_x == "x" and (root[0]+1 < nex[0] or root[1]+1 < nex[1]):
        dp[n_row][n_col] = (root[0]+1,root[1]+1)
        que.put((n_row,n_col))
def bomberman():
    n,k,ri,ci,rf,cf = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append(input())
    dp = [[(float("inf"),float("inf")) for i in range(n)] for e in range(n)]
    dp[ri][ci] = (0,0)
    que = queue.Queue(1000000)
    que.put((ri,ci))
    while(not que.empty()):
        node = que.get()
        row,clm = node
        if dp[row][clm][1] > k:
            continue
        if node == (rf,cf):
            print(dp[rf][cf][0])
            return 1
        if row > 0:
            check(dp,row,clm,row-1,clm,arr,que)
        if row < n-1:
            check(dp,row,clm,row+1,clm,arr,que)
        if clm > 0:
            check(dp,row,clm,row,clm-1,arr,que)
        if clm < n-1:
            check(dp,row,clm,row,clm+1,arr,que)
    
if not bomberman():
    print("Impossible")

