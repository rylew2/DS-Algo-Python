
# Operations
# ------------------
# BinaryHeap() creates a new, empty, binary heap.
# insert(k) adds a new item to the heap.
# find_min() returns the item with the minimum key value, leaving item in the heap.
# del_min() returns the item with the minimum key value, removing the item from the heap.
# is_empty() returns true if the heap is empty, false otherwise.
# size() returns the number of items in the heap.
# build_heap(list) builds a new heap from a list of keys.


class BinaryHeap(object):
    def __init__(self, initialval=0):
        self.items = [initialval] #initialize to allow us to do integer division floor

    def __len__(self):
        return len(self.items) - 1 # minus 1 to ignore first element

    def percolate_up(self):
        i = len(self)
        while i // 2 > 0:
            if self.items[i] < self.items[i // 2]:
                self.items[i // 2], self.items[i] = \
                    self.items[i], self.items[i // 2]
            i = i // 2

    def insert(self, k):
        self.items.append(k)
        self.percolate_up()

    def print(self):
        print(self.items)

bh = BinaryHeap()
bh.insert(2)
bh.insert(1)
bh.insert(0)
bh.print()