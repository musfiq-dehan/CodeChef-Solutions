# Test Case
t = int(input())

# Taking Inputs
for i in range(t):
    n, x = map(int, input().split())
    
    ti = 2**x 
    
    for _ in range(n):
        ti = ti//2
        
    print(ti)
