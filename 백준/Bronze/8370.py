import sys

sys.setrecursionlimit(10**6)

n1, k1, n2, k2 = map(int, sys.stdin.readline().split())

print(n1 * k1 + n2 * k2)
