import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().split()))

d = [1]*(n+1)

for i in range(1, n):
    for j in range(0, i):
        if a[j]<a[i]:
            if d[i]<=d[j]:
                d[i]=d[j]+1

print(max(d))