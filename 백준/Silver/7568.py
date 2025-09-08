import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]
res = []

for x,y in arr:
    count = 0
    for p,q in arr:
        if p>x and q>y:
            count += 1
    res.append(count+1)

print(*res)