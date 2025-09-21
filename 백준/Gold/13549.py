import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,k = map(int, input().split())
m = max(n,k)*2+2
graph = [[] for _ in range(m)]
distance = [INF]*(m)

for i in range(m):
    if i-1>=0:
        graph[i].append((i-1,1))
    if i+1<m:
        graph[i].append((i+1,1))
    if 2*i<m:
        graph[i].append((2*i,0))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(n)

print(distance[k])