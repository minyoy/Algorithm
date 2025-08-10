import sys

sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().rstrip().split())
    candy = map(int, sys.stdin.readline().split())

    res = []
    for i in candy:
        res.append(i // K)
    print(sum(res))
