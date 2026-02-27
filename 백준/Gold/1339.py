import sys
input = sys.stdin.readline

n = int(input())
alphabet = {}

a = [input().rstrip() for _ in range(n)]

for i in a:
    x = len(i)-1
    for j in i:
        if j in alphabet:
            alphabet[j] += 10**x
        else:
            alphabet[j] = 10**x
        x -= 1

sort_values = sorted(alphabet.values(), reverse=True)
result = 0
num = 9

for k in sort_values:
    result += k*num
    num -= 1

print(result)
