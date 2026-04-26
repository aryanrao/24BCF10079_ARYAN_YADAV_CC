t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    k = 0
    for x in a:
        if x == 1:
            k += 1
        else:
            break
    
    if k == n:
        if n % 2 == 1:
            print("First")    
        else:
            print("Second")   
    else:
        if k % 2 == 0:
            print("First")
        else:
            print("Second")
