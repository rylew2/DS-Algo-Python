
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# V , L , R
def preorder_recursive(root):
    if root:
        print(root.val, end=" => ")
        preorder_recursive(root.left)
        preorder_recursive(root.right)

# L , V , R
def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.val, end=" => ")
        inorder_recursive(root.right)

# L , R , V
def postorder_recursive(root):
    if root:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.val, end=" => ")


def preorder_iterative(root):
    curr = root
    stack = []

    while True:
        if curr:
            stack.append(curr)
            print(curr.val, end=" => ")
            curr = curr.left

        elif stack:
            curr = stack.pop()
            curr = curr.right
        else:
            break


def inorder_iterative(root):
    curr = root
    stack = []

    while True:
        if curr:
            stack.append(curr)
            curr = curr.left

        elif stack:
            curr = stack.pop()
            print(curr.val, end=" => ")
            curr = curr.right
        else:
            break

def postorder_iterative(root):
    if not root: return
    s1 = []
    s2 = []
    s1.append(root)

    while s1:
        curr = s1.pop()
        s2.append(curr.val)
        if curr.left:
            s1.append(curr.left)
        if curr.right:
            s1.append(curr.right)

    s2.reverse()
    print(s2)
    return


# n / 1
def Morris(root):
    # Set current to root of binary tree
    curr = root

    while curr:


        if not curr.left:
            # if curr doesn't have a left subtree, print data and move right
            print(curr.val)
            curr = curr.right
        else:
            # Find the previous (prev) of curr
            # 1. if current node has left child then find its in-order predecessor and make root as right child of it and move left of root.
            # 1 is root - so make (the inorder predecessor) 5's right child be the root
            prev = curr.left
            while (prev.right and prev.right != curr):
                prev = prev.right

            # Make curr as right child of its prev
            if not prev.right:
                prev.right = curr
                curr = curr.left

            # fix the right child of prev
            else:
                prev.right = None
                print(curr.val)
                curr = curr.right



root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)

Morris(root)
#
# preorder_recursive(root)
# print()
# preorder_iterative(root)
# print()
# print('====================')
# inorder_iterative(root)
# print()
# inorder_recursive(root)
# print()
# print('====================')
#
# postorder_iterative(root)


