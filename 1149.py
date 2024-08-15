import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    DP = [0] * 1001
    cost = list(map(int, input().strip()))
    