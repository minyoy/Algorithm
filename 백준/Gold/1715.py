from queue import PriorityQueue

import sys
input = sys.stdin.readline

n = int(input().strip())
queue = PriorityQueue(maxsize=100000)
result = 0

for _ in range(n):
    queue.put(int(input().strip()))
    
for i in range(queue.qsize()-1):
    w1 = queue.get()
    w2 = queue.get()
    queue.put(w1+w2)
    result += w1+w2

print(result)