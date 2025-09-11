import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().split()))
cost = list(map(int, input().split()))

count = 0
m = 10**6
res = 0

for i in range(n-1):
    if cost[i]<m: m = cost[i]
    res += m*arr[i]

print(res)
