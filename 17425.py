import sys
import math
input = sys.stdin.readline

T = int(input())

F = [0]*1000001
G = [0]*1000001

for i in range(1, 1000001):
    j = 1
    while i*j <= 1000000:
        F[i*j] += i
        j+=1
G[1] = 1
for i in range(2, 1000001):
    G[i] = F[i] + G[i-1]
    
for _ in range(T):
    N = int(input())
    print(G[N])