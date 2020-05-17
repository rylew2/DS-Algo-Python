# Bubble Sort
# time complexity: O(n^2)
# space complexity: O(1)


# range([start], stop[, step])
#     start: Starting number of the sequence.
#     stop: Generate numbers up to, but not including this number.
#     step: Difference between each number in the sequence.

def bubbleSort(alist):
    alreadySorted = False
    for passnum in range(len(alist)-1,0,-1): # range of list length to 1 . Inspect 1 less element each iteration
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alreadySorted = True
                alist[i], alist[i+1] = swap(alist[i], alist[i+1])

            if not alreadySorted:
                return alist


def swap(a,b):
    temp = a
    a = b
    b = temp
    return a, b


def bubbleSort2(alist):

    for end in range(len(alist)-1, 0, -1):
        alreadySorted = False
        for idx in range(end):
            if alist[idx] > alist[idx+1]:
                alreadySorted = True
                alist[idx], alist[idx+1] = alist[idx+1], alist[idx]

            if not alreadySorted:
                return alist



def selectionSort(alist):
    for start in range(len(alist)):
        min = start
        for i in range(start, len(alist)):
            if alist[i] < alist[min]:
                min = i
        alist[start], alist[min] = alist[min], alist[start]

    return alist







alist = [8,3,1,7,0]
selectionSort(alist)
print(alist)


alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)


alist = [8,3,1,7,0]
bubbleSort(alist)
print(alist)

alist = [1,2,3,4]
bubbleSort2(alist)
print(alist)


