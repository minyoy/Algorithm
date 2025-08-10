import sys

sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    h = int(sys.stdin.readline().rstrip())
    act = str(sys.stdin.readline().rstrip())
    b_count = act.count("b")
    c_count = act.count("c")

    res = h + c_count - b_count

    print(f"Data Set {i + 1}:\n{res}")
    if i != T - 1:
        print()
