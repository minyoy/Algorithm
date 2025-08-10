import sys

sys.setrecursionlimit(10**6)


def dfs(s, graph, visited, parent):
    visited[s] = 1

    for v in graph[s]:
        if not visited[v]:
            parent[v] = s
            dfs(v, graph, visited, parent)


N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
parent = [-1] * (N + 1)

for _ in range(N - 1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1, graph, visited, parent)
print(*parent[2:], sep="\n")
