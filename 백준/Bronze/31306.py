from collections import Counter

s = input().rstrip()

count = Counter(s)
result_in_y = 0
result_not_y = 0

for c in ['a','e','i','o','u','y']:
    if c == 'y':
        result_in_y+=count['y']
    else:
        result_in_y+=count[c]
        result_not_y+=count[c]

print(f'{result_not_y} {result_in_y}')