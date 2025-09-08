import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())
arr = sorted(list(map(int, sys.stdin.readline().split())))
sum_arr = [0]

for i in range(len(arr)):
    sum_arr.append(sum_arr[i]+arr[i])

print(sum(sum_arr))