import sys

sys.setrecursionlimit(10**6)


N = int(sys.stdin.readline().rstrip())
parent = list(map(int, sys.stdin.readline().split()))
del_node = []
node = [i for i in range(N)]
count = 0

n = int(sys.stdin.readline().rstrip())
del_node.append(n)
node.remove(n)
parent[n] = -2

while del_node != []:
    a = del_node.pop()
    for i in range(N):
        if a == parent[i]:
            del_node.append(i)
            node.remove(i)
            parent[i] = -2

for i in node:
    if i not in parent:
        count += 1

print(count)
