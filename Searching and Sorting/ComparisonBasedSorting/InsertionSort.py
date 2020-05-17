
import bisect

def insertion_sort(alist):
    for i in range(1,len(alist)):
        key = alist[i]
        j = i - 1


        while j>=0 and key< alist[j]:
            alist[j+1] = alist[j]
            j -= 1
        alist[j+1] = key





def selection_sort(alist):

    for curr_pos in range(len(alist)):
        min_idx = curr_pos
        for i in range(curr_pos+1, len(alist)):
            if alist[i] < alist[min_idx]:
                min_idx = i

        alist[curr_pos], alist[min_idx] = alist[min_idx], alist[curr_pos]



def binary_insertion_sort(alist):

    # n * 3n => n^2

    for i in range(1, len(alist)): # O(n)
        ins_idx = bisect.bisect(alist[:i], alist[i]) # n

        if ins_idx != i: # if the i'th num already in sorted order
            alist.insert(ins_idx, alist[i]) # n
            del alist[i+1] # n




alist = [4,1,3,2]
binary_insertion_sort(alist)
print(alist)

#
alist = [54,26,93,17,77,31,44,55,20]
binary_insertion_sort(alist)
print(alist)