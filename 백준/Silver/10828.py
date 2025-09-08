import sys
input = sys.stdin.readline

n = int(input().strip())
stack = []

def is_empty():
    return len(stack) == 0

for _ in range(n):
    commend = list(map(str, input().rstrip().split()))

    if commend[0] == 'push':
        stack.append(int(commend[1]))
    elif commend[0] == 'pop':
        if (is_empty()):
            print(-1)
        else:
            a = stack.pop()
            print(a)
    elif commend[0] == 'size':
        print(len(stack))
    elif commend[0] == 'empty':
        print(1 if is_empty() else 0)
    elif commend[0] == 'top':
        if (is_empty()):
            print(-1)
        else:
            print(stack[-1])