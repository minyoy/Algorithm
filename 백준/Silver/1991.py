import sys

sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preorder(root, order):
    if root.data != ".":
        order.append(root.data)
        preorder(tree[root.left], order)
        preorder(tree[root.right], order)


def inorder(root, order):
    if root.data != ".":
        inorder(tree[root.left], order)
        order.append(root.data)
        inorder(tree[root.right], order)


def postorder(root, order):
    if root.data != ".":
        postorder(tree[root.left], order)
        postorder(tree[root.right], order)
        order.append(root.data)


N = int(sys.stdin.readline().rstrip())
nodeinfo = [[*(map(str, sys.stdin.readline().split()))] for _ in range(N)]
tree = {".": Node(".", None, None)}

for info in nodeinfo:
    tree[info[0]] = Node(*info)

preorder_list = []
preorder(tree["A"], preorder_list)

inorder_list = []
inorder(tree["A"], inorder_list)

postorder_list = []
postorder(tree["A"], postorder_list)

print("".join(preorder_list))
print("".join(inorder_list))
print("".join(postorder_list))
