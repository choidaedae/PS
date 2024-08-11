import heapq
import sys 

N = int(sys.stdin.readline().rstrip())
inputs = []
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if len(inputs) ==0: print(0)
        else:
            print(-heapq.heappop(inputs))
    else:
        heapq.heappush(inputs, num)
    
