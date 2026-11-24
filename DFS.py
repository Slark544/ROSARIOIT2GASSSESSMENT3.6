
# Binary Tree using ROSARIO CLARK

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# DFS - PreOrder Traversal
def DFS(root):
    if root is None:
        return

    print(root.data, end=" ")
    DFS(root.left)
    DFS(root.right)


# Create Binary Tree
root = Node("ROSARIO")

root.left = Node("CLARK")
root.right = Node("S")

root.left.left = Node("R")
root.left.right = Node("I")

root.right.left = Node("A")
root.right.right = Node("O")


# Display DFS
print("DFS Traversal:")
DFS(root)
