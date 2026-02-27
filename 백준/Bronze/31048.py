import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def last_factorial(n):
    if n==1:
        return 1
    return n*last_factorial(n-1)%10

t = int(input())
for _ in range(t):
    n = int(input())
    print(last_factorial(n))