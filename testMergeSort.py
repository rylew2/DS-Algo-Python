

def mergesort(alist):
    if len(alist)>1: # stop recursion when we're down to 1 item in list
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        merge(alist, lefthalf, righthalf)


def merge(alist, lefthalf, righthalf):
    i = 0;
    j = 0;
    k = 0;
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[k] = lefthalf[i]
            i += 1
        else:
            alist[k] = righthalf[j]
            j += 1
        k += 1
    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i += 1
        k += 1
    while j < len(righthalf):
        alist[k] = righthalf[j]
        j += 1
        k += 1


alist = [4,3,2,1]
# alist = [54,26,93,17,77,31,44,55,20]
mergesort(alist)
print(alist)