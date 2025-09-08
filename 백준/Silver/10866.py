import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
dq = deque([])

def is_empty():
    return len(dq) == 0

for _ in range(n):
    commend = list(map(str, input().rstrip().split()))

    if commend[0] == 'push_front':
        dq.appendleft(int(commend[1]))
    elif commend[0] == 'push_back':
        dq.append(int(commend[1]))
    elif commend[0] == 'pop_front':
        if (is_empty()):
            print(-1)
        else:
            print(dq.popleft())
    elif commend[0] == 'pop_back':
        if (is_empty()):
            print(-1)
        else:
            print(dq.pop())
    elif commend[0] == 'size':
        print(len(dq))
    elif commend[0] == 'empty':
        print(1 if is_empty() else 0)
    elif commend[0] == 'front':
        if (is_empty()):
            print(-1)
        else:
            print(dq[0])
    elif commend[0] == 'back':
        if (is_empty()):
            print(-1)
        else:
            print(dq[-1])
