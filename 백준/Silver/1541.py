import sys

sys.setrecursionlimit(10**6)

arr1 = list(map(str, sys.stdin.readline().strip().split('-')))
arr2 = []
result = 0

for c in arr1:
    if '+' in str(c):
        temp = list(map(int, c.split('+')))
        arr2.append(sum(temp))
    else:
        arr2.append(int(c))

for i in range(len(arr2)):
    if i != 0:
        result -= arr2[i]
    else:
        result = arr2[i]

print(result)