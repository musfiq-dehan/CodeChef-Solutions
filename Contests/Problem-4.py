# Test Case
t = int(input())

# Taking Inputs
for i in range(t):
    n, x, c = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    print(sum(max(j, x-c) for j in arr))
