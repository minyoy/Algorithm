import sys
from collections import Counter
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
s = ""
c = 0

for i in range(m):
    a = [r[i] for r in arr]
    r = sorted(Counter(a).most_common(), key=lambda x: (-x[1], x[0]))
    s += r[0][0]
    c += n-r[0][1]

print(s)
print(c)