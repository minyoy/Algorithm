import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[0], x[1]))

heap = [arr[0][1]]

for a,b in arr[1:]:
    if heap[0] <= a:
        heapq.heappop(heap)
    heapq.heappush(heap, b)
    
print(len(heap))