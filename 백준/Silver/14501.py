import sys 
input = sys.stdin.readline 
n = int(input().strip()) 
arr = [list(map(int, input().split())) for _ in range(n)] 
d = [0]*n 
for i in range(n): 
    for j in range(i+arr[i][0]-1, n): 
        d[j] = max(d[j], d[i]+arr[j][1]) 
            
print(d[-1])