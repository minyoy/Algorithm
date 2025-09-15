import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]

d = [0]*(n+1)

for i in range(n):
    for j in range(i+arr[i][0], n+1):
        if d[j]<d[i]+arr[i][1]:
            d[j] = d[i]+arr[i][1]

print(d[-1])