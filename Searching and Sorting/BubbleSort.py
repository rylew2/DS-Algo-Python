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

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


alist = [8,3,1,7,0]
bubbleSort(alist)
print(alist)

alist = [1,2,3,4]
bubbleSort(alist)
print(alist)


