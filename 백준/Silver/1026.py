import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())
a = sorted(list(map(int, sys.stdin.readline().split())))
b = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
sum_arr = []

for i in range(n):
    sum_arr.append(a[i]*b[i])

print(sum(sum_arr))