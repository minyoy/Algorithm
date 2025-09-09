import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def num_set():
    num_arr = list(range(0,10))
    num_arr.append(6)
    num_arr.remove(9)
    return num_arr

arr = list(map(int, input().rstrip()))
current_num_arr = num_set()
count = 1

for i in arr:
    if i == 9:
        i = 6
    
    if i not in current_num_arr:
        count += 1
        current_num_arr += num_set()
    current_num_arr.remove(i)

print(count)
