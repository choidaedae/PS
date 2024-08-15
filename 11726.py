import sys 
input = sys.stdin.readline

N = int(input().rstrip())

DP = [0]*1001
DP[1] = 1; DP[2] = 2
for i in range(3, 1001):
    DP[i] = (DP[i-1] + DP[i-2]) % 10007
    
print(DP[N])