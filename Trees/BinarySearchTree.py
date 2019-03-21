class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        # allow duplicates with via a count
        # https://www.geeksforgeeks.org/how-to-handle-duplicates-in-binary-search-tree/
        self.count = 1


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current = self.root

        while 1:
            if new_val == current.value:
                current.count += 1
                return
            elif new_val > current.value:
                if current.right == None:
                    current.right = Node(new_val)
                    return
                current = current.right
            else:
                if current.left == None:
                    current.left = Node(new_val)
                    return
                current = current.left

    def insertRecursive(self, new_val, currentNode = None ):
        if currentNode == None:
            current=  self.root
        else:
            current = currentNode


        if new_val == current.value:
            current.count += 1
            return
        elif new_val > current.value:
            if current.right == None:
                current.right = Node(new_val)
                return
            current = current.right
            self.insertRecursive(new_val, current)
        else:
            if current.left == None:
                current.left = Node(new_val)
                return
            current = current.left
            self.insertRecursive(new_val, current)

    def search(self, find_val):
        current = self.root
        while 1:
            if current.left == None and current.right == None:
                return False

            if find_val == current.value:
                return True

            if find_val > current.value:
                current = current.right
            elif find_val< current.value:
                current = current.left

        return False




# Set up tree
tree = BST(4)

# Insert elements
# tree.insert(2)
# tree.insert(1)
# tree.insert(3)
# tree.insert(5)


tree.insertRecursive(4)
tree.insertRecursive(2)
tree.insertRecursive(1)
tree.insertRecursive(3)
tree.insertRecursive(5)


# Check search
# Should be True
print(tree.search(4))

# Should be False
print(tree.search(6))