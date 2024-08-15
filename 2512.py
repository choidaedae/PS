import sys

N = int(sys.stdin.readline().rstrip())

requires = list(map(int, sys.stdin.readline().rstrip().split()))

budget = int(sys.stdin.readline().rstrip())
if sum(requires) <= budget:
    print(max(requires))
else: 
    upper_bound = max(requires)
    lower_bound = 1
    while lower_bound <= upper_bound:
        money = 0
        middle = (lower_bound + upper_bound) //2
        for require in requires:
            if middle >= require: money += require
            else:
                money += middle
        if money > budget: 
            upper_bound = middle-1
        else: 
            result = middle
            lower_bound = middle+1
    print(result)
                
        
    
    
 