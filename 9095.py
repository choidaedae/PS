DP = [0] * 12
DP[1] = 1
DP[2] = 2
DP[3] = 4

for i in range(4, 11):
    DP[i] = DP[i-1] + DP[i-2] + DP[i-3]

T = int(input())

for i in range(T):
    N = int(input())
    print(DP[N])



