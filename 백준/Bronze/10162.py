import sys

sys.setrecursionlimit(10**6)

count = [0]*3
t = int(sys.stdin.readline().rstrip())

btn_types = [300, 60, 10]

for i in range(len(btn_types)):
    count[i] += t // btn_types[i]
    t %= btn_types[i]

if t == 0:
    print(*count)
else:
    print(-1)
