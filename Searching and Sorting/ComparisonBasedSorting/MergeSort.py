def mergeSort(alist):
    if len(alist)>1: # stop when we're down to 1 item
        mid = len(alist)//2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0 # i ==> lefthalf index marker
        j=0 # j ==> right index marker
        k=0 # k ==> alist index marker (increment on every alist update)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k]=left[i]
                i=i+1
            else:
                alist[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            alist[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            alist[k]=right[j]
            j=j+1
            k=k+1

# alist = [4,3,2,1]
alist = [8,3,1,10,12,5]
mergeSort(alist)
print(alist)
