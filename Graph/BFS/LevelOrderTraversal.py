# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque,OrderedDict


# N / N
def bfsLevelOrder(root):
    level = 0
    levels = []
    q = deque([root])
    while q:
        levLength = len(q)
        levels.append([])
        for i in range(levLength):
            v = q.popleft()
            levels[level].append(v)
            if v.left: q.append(v.left)
            if v.right: q.append(v.right)
        level += 1

    return levels


t = TreeNode(3)
t.left=TreeNode(9)
t.right=TreeNode(20)
t.right.left=TreeNode(15)
t.right.right=TreeNode(7)

print(bfsLevelOrder(t))

# simplest  N / 1
# succ = None
# while root:  # loop will end when we move right or left into None
#
#     # p is less than root/curr , save possible successor
#     if root.val > p.val:
#         succ = root
#         root = root.left
#
#     else:  # else just move to the right
#         root = root.right
#
#     return succ




