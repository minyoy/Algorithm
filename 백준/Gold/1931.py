import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end = -1

for a,b in arr:
    if a >= last_end:
        count += 1
        last_end = b

print(count)