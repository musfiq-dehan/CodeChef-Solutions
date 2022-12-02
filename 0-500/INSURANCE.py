# Test Case
t = int(input())

# Taking Inputs
for i in range(t):
    x, y = map(int, input().split())
    
    print(min(x, y))
