



class Node:
    def __init__(self, x = None):
        self.val = x
        self.next = None
        self.prev =  None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, x: Node):
        if self.head==None:
            self.head = x
            self.tail = self.head
            self.size = 1

        else:
            x.prev = self.tail
            self.tail.next = x
            self.tail = x
            self.size+=1

    def dequeue(self):
        if self.head == None:
            return None
        else:
            d = self.head
            if self.size>1:
                self.head.next.prev = None
            self.head = self.head.next
            d.next = None
            self.size -= 1
            return d

    def print_q(self):
        curr = self.head
        while curr:
            print('{} => '.format(curr.val), end='')
            curr = curr.next

        print('None')




q = Queue()
q.enqueue(Node(1))
q.enqueue(Node(2))
q.enqueue(Node(3))
q.enqueue(Node(4))
q.dequeue()
q.dequeue()
zz= 2
q.print_q()

