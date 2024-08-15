import sys
import math 

input = sys.stdin.readline
DP = [0] * 91
DP[1] = 1
DP[2] = 1
N = int(input())
for i in range(3, 91):
    DP[i] = DP[i-1] + DP[i-2]
print(DP[N])