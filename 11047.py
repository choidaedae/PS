import sys

inputs = sys.stdin.readline().rstrip()
N = int(inputs.split()[0]); K = int(inputs.split()[1])
coins = []
ans = 0
for i in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))
coins.reverse()
for coin in coins:
    if K >= coin:
        ans += K // coin  
        K -= coin * (K // coin)  
    
    if(K == 0): 
        print(ans)
        break

