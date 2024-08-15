import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    DP = [0] * 1001
    costs = list(map(int, input().strip()))
    for color, cost in enumerate(costs):
        DP[color] = cost
        for i in range(2, 1001):
            DP[i] = max(DP[i-1])
    