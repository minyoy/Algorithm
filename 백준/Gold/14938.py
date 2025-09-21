import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,r=map(int, input().split())
t = list(map(int, input().split()))

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(r):
    a,b,c=map(int, input().split())
    graph[a][b]=c
    graph[b][a]=c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result=[]
for a in range(1,n+1):
    s=0
    for b in range(1,n+1):
        if graph[a][b]<=m:
            s+=t[b-1]
    result.append(s)
print(max(result))