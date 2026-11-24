
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
root = Node("R")
root.left = Node("O")
root.right = Node("S")

root.left.left = Node("A")
root.left.right = Node("R")

root.right.left = Node("I")
root.right.right = Node("O")

root.left.left.left = Node("C")
root.left.left.right = Node("L")
root.right.left.left = Node("A")
root.right.left.right = Node("R")
root.right.right.left = Node("K")


# PreOrder
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# InOrder
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# PostOrder
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


print("PREORDER:")
preorder(root)

print("\nINORDER:")
inorder(root)

print("\nPOSTORDER:")
postorder(root)
