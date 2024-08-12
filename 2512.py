import sys

inputs = sys.stdin.readline().rstrip()

N = int(inputs.split()[0]); M = int(inputs.split()[1])

map = [[0 for _ in range(N+1)] for _ in range(N+1)]
sum = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    nums = sys.stdin.readline().rstrip().split()
    for j, num in enumerate(nums):
        map[i][j+1] = int(num)
        
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == 1 and j == 1: sum[i][j] = map[i][j]
        elif i == 1: sum[i][j] = sum[i][j-1] + map[i][j]
        elif j == 1: sum[i][j] = sum[i-1][j] + map[i][j]
        else: sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + map[i][j]
                
ans_list = []
for i in range(M):
    coords = sys.stdin.readline().rstrip().split()
    x1 = int(coords[0])
    y1 = int(coords[1])
    x2 = int(coords[2])
    y2 = int(coords[3])
    if x1 == 1 and y1 ==1:
        ans = sum[y2][x2]
    elif x1 == 1:
        ans = sum[y2][x2] - sum[y1-1][x1-1]
    elif y1 == 1:
        ans = sum[y2][x2] - sum[y1-1][x1-1]
    else:
        ans = sum[y2][x2] - sum[y1][x1-1] - sum[y1-1][x1] + sum[y1-1][x1-1]
    ans_list.append(ans)
    
print(ans_list)
    
    
 