import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = [int(input().rstrip()) for _ in range(n)]

d = [0]*n

if n==1:
    print(a[0])
elif n==2:
    print(a[0]+a[1])
elif n==3:
    print(max(a[0]+a[2], a[1]+a[2]))
else:
    d[0]=a[0]
    d[1]=a[0]+a[1]
    d[2]=max(a[0]+a[2], a[1]+a[2])
    for i in range(3,n):
        d[i]=max(d[i-2]+a[i], d[i-3]+a[i-1]+a[i])
    
    print(d[n-1])