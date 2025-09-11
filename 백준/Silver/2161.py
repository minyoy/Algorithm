import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
num = deque([i for i in range(1, n+1)])
res = []

for j in range(n-1):
    res.append(num.popleft())
    num.append(num.popleft())

res += num
print(*res)