import heapq
import sys 

N = int(sys.stdin.readline().rstrip())
pheap = []
mheap = []
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if len(pheap) == 0 and len(mheap) == 0: print(0)
        elif len(pheap) == 0: print(-heapq.heappop(mheap))
        elif len(mheap) == 0: print(heapq.heappop(pheap))
        else: 
            num1 = heapq.heappop(mheap)
            num2 = heapq.heappop(pheap)
            if num1 < num2:
                print(-num1)
                heapq.heappush(pheap, num2)
            elif num1 > num2:
                print(num2)
                heapq.heappush(mheap, num1)
            else:
                print(-num1)
                heapq.heappush(pheap, num2)
    elif num > 0:
        heapq.heappush(pheap, num)
    else: 
        heapq.heappush(mheap, -num)
    
