n,x = map(int, input().split())
result = []

for _ in range(n):
    s,t = map(int, input().split())
    if s+t<=x:
        result.append((s,t))

result.sort(key=lambda x: x[0], reverse=True)

if len(result) == 0:
    print(-1)
else:
    print(result[0][0])