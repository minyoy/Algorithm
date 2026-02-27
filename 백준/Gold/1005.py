import sys
from collections import deque
import copy
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    time = list(map(int, input().split()))
    indegree = [0]*(n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(k):
        a,b = map(int, input().split())
        graph[a].append(b)
        indegree[b]+=1

    def topology_sort(k):
        result = copy.deepcopy(time)
        q = deque()

        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            now = q.popleft()
            for i in graph[now]:
                result[i-1] = max(result[i-1], result[now-1]+time[i-1])
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        print(result[k-1])

    k = int(input())
    topology_sort(k)