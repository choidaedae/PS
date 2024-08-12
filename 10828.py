import sys 

N = int(sys.stdin.readline().rstrip()) 

stack = []

for i in range(N):
    line = sys.stdin.readline().rstrip()
    instruction = line.split()[0]
    if len(line.split()) == 2:
        num = int(line.split()[1])
    if instruction == "push":
        stack.append(num)
    elif instruction == "pop":
        if len(stack) == 0: 
            print(-1)
        else:
            print(stack.pop())
    elif instruction == "size":
        print(len(stack))
    elif instruction == "empty":
        print(int(len(stack)==0))
    elif instruction == "top":
        if len(stack) == 0: 
            print(-1)
        else:
            print(stack[-1])