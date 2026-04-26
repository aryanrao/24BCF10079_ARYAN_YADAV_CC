t = int(input())

for _ in range(t):
    n = int(input())
    
    if n == 2:
        print(-1)
        continue
    
    nums = []
    
    # Add odds
    for i in range(1, n*n + 1, 2):
        nums.append(i)
    
    # Add evens
    for i in range(2, n*n + 1, 2):
        nums.append(i)
    
    # Fill matrix
    for i in range(n):
        print(*nums[i*n:(i+1)*n])
