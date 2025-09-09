import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split())
r = []

def solution(s):
    if len(r) == m:
        print(*r)
        return
    for i in range(s, n+1):
        if i not in r:
            r.append(i)
            solution(i+1)
            r.pop()

solution(1)