import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

def fib(n):
    if n<0: return 0
    if n==1: return 1
    return fib(n-1)+fib(n-2)

fib=memoize(fib)

t = int(input().rstrip())
for _ in range(t):
    m = int(input().rstrip())
    
    if m == 0:
        print(1, 0)
    else:
        i = fib(m-1)
        j = fib(m+1)
        print(i, j-i)
