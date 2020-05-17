
class Element:
    def __init__(self, val):
        self.value = val
        self.next = None

    def print(self):
        print(self.val)

class MyLinkedList():
    def __init__(self, head=None):
        self.head = head
        if head!=None:
            self.size = 1
        else:
            self.size = 0

    # add an element to the end
    def append(self, elem):
        curr = self.head
        if curr:
            while curr.next: # move curr to last node
                curr = curr.next

            curr.next = elem
        else:
            self.head = elem
        self.size += 1


    def get_position(self, pos):
        if pos<1 or pos > self.size:
            return None
        counter = 1
        curr = self.head
        while curr and counter<=pos:
            if counter == pos:
                return curr
            curr = curr.next
            counter += 1
        return None


    def insert(self, elem, pos):
        if pos < 1 or pos>(self.size+1):
            print('invalid position specified on insert')
            return None
        if pos == 1:
            elem.next = self.head
            self.head = elem
        else:
            counter = 1
            curr = self.head
            prev = None
            while curr and counter<pos-1:
                curr = curr.next
                counter += 1

            elem.next = curr.next
            curr.next = elem

        self.size += 1


    def delete(self, pos):
        if pos < 1 or pos > (self.size + 1):
            print('invalid position specified on insert')
            return None

        curr = self.head
        if pos == 1:
            self.head = curr.next
            curr.next = None
        else:
            counter = 1
            while curr and counter<pos-1:
                curr = curr.next
                counter+=1

            next = curr.next
            curr.next = curr.next.next
            next.next = None
        self.size -= 1

# 3,3,4,2,4,3

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
print('append 1')
ll = MyLinkedList(e1)
print('append 2')
ll.append(e2)
print('append 3')
ll.append(e3)
print('ll size: ' + str(ll.size))
ll.append(e4)

ll.insert(Element(99), 3)

ll.delete(3)


ll.insert(Element(99), 5)
ll.delete(5)

ll.delete(1)


x=2
