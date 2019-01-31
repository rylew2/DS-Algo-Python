def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1: # stop when we're down to 1 item
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0 # i ==> lefthalf index marker
        j=0 # j ==> righthalf index marker
        k=0 # k ==> alist index marker (increment on every alist update)
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [4,3,2,1]
# alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
