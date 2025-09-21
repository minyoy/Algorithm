from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n,k = map(int, input().split())
visited=[False]*100001

def bfs(start, visited):
    queue = deque([(start,0)])
    visited[start]=True
    while queue:
        x, dist = queue.popleft()
        if x==k:
            print(dist)
            break
        if 0<=2*x<=100_000 and not visited[2*x]:
            queue.appendleft((2*x, dist))
            visited[2*x]=True
        for nx in [x-1,x+1]:
            if 0<=nx<=100_000 and not visited[nx]:
                queue.append((nx, dist+1))
                visited[nx]=True

bfs(n, visited)