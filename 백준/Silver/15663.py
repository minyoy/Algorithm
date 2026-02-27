import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split())
num_lst = sorted(list(set(map(int, input().split()))))
r = []

def backtrack(s):
    if len(r) == m:
        print(*r)
        return
    
    for i in num_lst:
        if s<=i:
            r.append(i)
            backtrack(i)
            r.pop()

backtrack(1)