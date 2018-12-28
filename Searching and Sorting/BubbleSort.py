# Bubble Sort
# time complexity: O(n^2)
# space complexity: O(1)


# range([start], stop[, step])
#     start: Starting number of the sequence.
#     stop: Generate numbers up to, but not including this number.
#     step: Difference between each number in the sequence.

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp




alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


alist = [8,3,1,7,0]
bubbleSort(alist)
print(alist)


for x in range(len(alist)-1,0,-1):
    print(x)