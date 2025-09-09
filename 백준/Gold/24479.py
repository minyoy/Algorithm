import sys
from collections import deque
input = sys.stdin.readline

INF = 10**6

n = int(input().rstrip())
s = 2
t = 0
count = 0
v = (0,0)

graph = []
f_c = [[] for _ in range(7)]
for i in range(n):
    m = list(map(int, input().split()))
    graph.append(m)
    for j in range(len(m)):
        if m[j] == 9:
            v = (i,j)
            graph[i][j] = 0
        elif m[j] <=6 and m[j] >= 1:
            f_c[m[j]].append((i,j))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 이동 결정
def bfs(sx,sy,ex,ey):
    global s, t, count, v
    q = deque()
    visited = [[-1]*n for _ in range(n)]

    visited[sx][sy] = 0
    q.append((sx,sy))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 지도를 벗어나는 경우
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            # 내 사이즈보다 큰 물고기가 있는 경우 
            if graph[nx][ny] > s:
                continue
            # 방문을 안했고, 내 사이즈보다 작거나 같은 물고기가 있는 경우
            if visited[nx][ny] == -1:
                # 내 사이즈랑 같거나 0인 경우는 이동, 1초 추가
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                
                # 목적지에 도달했다면 종료
                if (nx==ex and ny==ey):
                    t += visited[nx][ny]

                    # 내 사이즈보다 작거나 0이 아닌 경우는 잡아먹음
                    # 빈칸으로 바꾸고 먹은 마리 수를 1 추가
                    # 만약에 먹은 마리 수가 크기랑 같다면 사이즈를 1 추가하고 먹은 마리 수 초기화
                    if 0 < graph[nx][ny] < s:
                        graph[nx][ny] = 0
                        count += 1
                        if count == s:
                            s += 1
                            count = 0

                    # 현재 위치를 도착 위치로 변경
                    v = (ex, ey)
                    return
    return

# 최단 거리 계산
def shortest_path(sx,sy,ex,ey):
    global s
    q = deque()
    q.append((sx,sy))

    visited = [[-1]*n for _ in range(n)]
    visited[sx][sy] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 지도를 벗어나는 경우
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            # 내 사이즈보다 큰 물고기가 있는 경우 
            if graph[nx][ny] > s:
                continue
            # 내 사이즈보다 작거나 같은 물고기가 있는 경우
            if visited[nx][ny] == -1:
                # 내 사이즈랑 같거나 0인 경우는 이동, 거리 1 추가
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                
                # 목적지에 도달했다면 종료
                if (nx==ex and ny==ey):
                    return visited[nx][ny]
    return -1 # 목적지에 도달하지 못함

while True:
    candidates = []
    
    for size_idx in range(min(s, 7)):
        for j, (r, c) in enumerate(f_c[size_idx]):
            d = shortest_path(v[0], v[1], r, c)
            if d != -1:
                candidates.append((d, r, c, size_idx, j))

    if len(candidates) == 0: break
    elif len(candidates) == 1:
        _, r, c, size_idx, j = candidates[0]
        del f_c[size_idx][j]
        bfs(v[0], v[1], r, c)
    else:
        candidates.sort(key=lambda x: (x[0], x[1], x[2]))
        _, r, c, size_idx, j = candidates[0]
        del f_c[size_idx][j]
        bfs(v[0], v[1], r, c)

print(t)
