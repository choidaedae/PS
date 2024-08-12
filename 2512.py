import sys

N = int(sys.stdin.readline().rstrip())

requires = map(sys.stdin.readline().rstrip().split(), int)

budget = int(sys.stdin.readline().rstrip())

if sum(requires) <= budget:
    print(max(requires))
else: 
    upper_bound = max(requires) * 2 
    money_sum = budget + 1
    while True:
        money_sum = 0
        for require in requires:
            if require < upper_bound:
                money_sum += require
            else: 
                money_sum += upper_bound 
                
        if money_sum > budget: 
            lower_bound = upper_bound 
            upper_bound = upper_bound
                
        
    
    
 