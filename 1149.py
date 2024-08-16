import sys
input = sys.stdin.readline

DP = [[0] * 1001 for _ in range(3)]
costs = [[0] * 1001 for _ in range(3)]

N = int(input())
for i in range(1, N+1):
    inputs = list(map(int, input().rstrip().split()))
    for color, cost in enumerate(inputs):
        costs[color][i] = cost
for i in range(1, N+1):
    DP[0][i] = costs[0][i] + min(DP[1][i-1], DP[2][i-1])
    DP[1][i] = costs[1][i] + min(DP[0][i-1], DP[2][i-1])
    DP[2][i] = costs[2][i] + min(DP[0][i-1], DP[1][i-1])
print(min([DP[0][N], DP[1][N], DP[2][N]]))
       