import sys

sys.setrecursionlimit(10**6)

count = 0
n = int(sys.stdin.readline().rstrip())
m = 1000 - n

coin_types = [500, 100, 50, 10, 5, 1]

for c in coin_types:
    count += m // c
    m %= c

print(count)