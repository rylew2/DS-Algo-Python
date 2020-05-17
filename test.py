
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# V, L , R
def preOrder(n):
    if n:
        print(n.val, end=' => ')
        preOrder(n.left)
        preOrder(n.right)

# L, V, R
def inOrder(n):
    if n:
        inOrder(n.left)
        print(n.val, end=' => ')
        inOrder(n.right)


# L, R, V
def postOrder(n):
    if n:
        postOrder(n.left)
        postOrder(n.right)
        print(n.val, end=' => ')




n = Node(4)
n.left = Node(2)
n.left.left = Node(1)
n.left.right = Node(3)
n.right = Node(6)
n.right.left = Node(5)
n.right.right = Node(7)

print('preorder')
preOrder(n)
print()
print()
print('inorder')
inOrder(n)
print()
print()
print('postorder')
postOrder(n)

