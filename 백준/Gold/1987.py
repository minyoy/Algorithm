import sys
input = sys.stdin.readline

r,c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
current_alpha = set()

max_count = 0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,count):
    global max_count
    max_count = max(max_count, count)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<r and 0<=ny<c:
            if graph[nx][ny] not in current_alpha:
                current_alpha.add(graph[nx][ny])
                dfs(nx,ny, count+1)
                current_alpha.remove(graph[nx][ny])

current_alpha.add(graph[0][0])
dfs(0,0,1)
print(max_count)