import sys

N = int(sys.stdin.readline().rstrip())

inputs = sys.stdin.readline().rstrip().split()

for i in range(N):
    inputs[i] = int(inputs[i])
    
inputs = sorted(inputs)
ans = 0

for i in range(N):
    ans += sum(inputs)
    inputs.pop()
    
print(ans)
    