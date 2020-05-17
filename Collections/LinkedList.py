"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        if head != None:
            self.size = 1
        else:
            self.size = 0

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next: # iterate to the last item
                current = current.next
            current.next = new_element
        else:
            self.head = new_element #empty LL, just set the head to the new element
        self.size+=1

    def get_position(self, position):
        if position < 1 or position > self.size:
            return None
        counter = 1
        current = self.head
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):   #ll.insert(e4, 3)
        if position < 1 or position > (self.size+1):
            print('Invalid position specified')
            return None
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1: #insert as head
            new_element.next = self.head
            self.head = new_element
        self.size+=1

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next: #iterate until we get to the value
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else: # delete the first element
                self.head = current.next
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
ll = LinkedList(e1)
print('append 2')
ll.append(e2)
print('append 3')
ll.append(e3)
print('ll size: ' + str(ll.size))

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

print('ll get position 4: ' + str(ll.get_position(4).value)) if ll.get_position(4)!=None else print('Attempted to retrieve invalid position 4, LL is only of size ' + str(ll.size))
#
# Test insert
print('insert e4 at position 3')
ll.insert(e4, 3)
print('ll size: ' + str(ll.size))

# Should print 4 now
print(ll.get_position(3).value)


# Test delete
print('delete at position 1')
ll.delete(1)
print('ll size: ' + str(ll.size))
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)