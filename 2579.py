import sys

input = sys.stdin.readline

N = int(input())

s = [0] * 301
for i in range(1, N+1):
    s[i] = int(input())

DP = [0] * 301
DP[1] = s[1]
DP[2] = s[1] + s[2]
DP[3] = max(s[1] + s[3], s[2] + s[3])

for i in range(4, N+1):
    DP[i] = max(DP[i - 3] + s[i - 1] + s[i], DP[i - 2] + s[i])

print(DP[N])