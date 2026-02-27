import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    count = 0
    for _ in range(n):
        v, f, c = map(int, input().split())
        if v*f/c>=d:
            count += 1
    print(count)
