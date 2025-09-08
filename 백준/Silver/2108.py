import sys
from collections import Counter
input = sys.stdin.readline

n = int(input().strip())
arr = [int(input().strip()) for _ in range(n)]
sorted_arr = sorted(arr)
res = []

res.append(round(sum(arr)/n))
res.append(sorted_arr[(n-1)//2])

# 처음에는 최빈값을 함수로 구현했으나 시간 초과로인해 Counter 기능 사용 
cnt = Counter(sorted_arr).most_common(2)
res.append((cnt[1][0] if cnt[0][1] == cnt[1][1] else cnt[0][0]) if len(arr)>1 else arr[0])

res.append(sorted_arr[n-1]-sorted_arr[0])

print(*res, sep='\n')