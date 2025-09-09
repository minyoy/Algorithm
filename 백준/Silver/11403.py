import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().rstrip())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def is_path(i,j):
    q = deque([i])
    visited = [0]*n

    while q:
        v = q.popleft()
        for c in range(n):
            if graph[v][c] == 1 and not visited[c]:
                q.append(c)
                visited[c] = 1
                if c == j:
                    return 1
    return 0

res = [[0]*n for _ in range(n)]
for a in range(n):
    for b in range(n):
        res[a][b] = is_path(a, b)

for r in res:
    print(*r, sep=" ")