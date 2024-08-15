import sys

input = sys.stdin.readline

N = int(input())


DP = [[0] * (N) for _ in range(N)]
array = [[0] * (N) for _ in range(N)]

for i in range(N):
    inputs = list(map(int, input().rstrip().split()))
    for j in range(i+1):
        array[i][j] = inputs[j]
   
DP[0][0] = array[0][0]     
for i in range(N):
    for j in range(i+1):
        if j == 0: 
            DP[i][j] = DP[i-1][j] + array[i][j]
        elif j == i:
            DP[i][j] = DP[i-1][j-1] + array[i][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-1]) + array[i][j] 

if N ==1:
    print(array[0][0])
else:   
    print(max(DP[N-1]))