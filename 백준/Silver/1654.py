import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [int(input().rstrip()) for _ in range(n)]

start = 1
end = max(arr)

result = 0
while(start<=end):
    total=0
    mid=(start+end)//2
    for x in arr:
        total+=(x//mid)
        
    if total<m:
        end=mid-1
    else:
        start=mid+1

print(end)