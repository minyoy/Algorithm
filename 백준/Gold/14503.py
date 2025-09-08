import sys
input = sys.stdin.readline

n,m = map(int, input().split())

d = [[0]*m for _ in range(n)]

x,y,direction = map(int, input().split())
d[x][y] = 1

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

def is_empty():
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if d[nx][ny] == 0 and arr[nx][ny] == 0:
            return True
    return False

count = 1
while True:
    if d[x][y] == 0: 
        d[x][y] = 1
        count += 1

    if (is_empty()):
        turn_left()
        mx = x+dx[direction]
        my = y+dy[direction]

        if d[mx][my] == 0 and arr[mx][my] == 0:
            x = mx
            y = my
            d[x][y] = 1
            count += 1
    else:
        nx = x-dx[direction]
        ny = y-dy[direction]

        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break

print(count)