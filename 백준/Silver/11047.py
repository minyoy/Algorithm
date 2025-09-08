import sys

sys.setrecursionlimit(10**6)

n, k = map(int, sys.stdin.readline().rstrip().split())
coin_types = []
count = 0

for i in range(n):
    coin_types.insert(0, int(sys.stdin.readline().rstrip()))

for c in coin_types:
    count += k // c
    k %= c

print(count)