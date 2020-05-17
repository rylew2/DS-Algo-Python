
def bsIterative(arr, l, r, x):
    while l<=r:
        mid = l + (r-l)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid+1
        else:
            r = mid-1
    return -1


# return idx of x. if it's not in the list, return -1
def bsRecursive(arr, l, r, x):
    if l<=r:
        mid = l + (r-l)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return bsRecursive(arr, mid+1, r, x)
        else:
            return bsRecursive(arr, l, mid-1, x)
    else:
        return -1


arr = [1,2,3,4,5]
print(bsIterative( arr, 0 , len(arr)-1, 4) )
print(bsRecursive( arr, 0 , len(arr)-1, 4) )
print(bsRecursive( arr, 0 , len(arr)-1, 2) )
print('-------------------------------')
print(bsIterative( arr, 0 , len(arr)-1, 10) )
print(bsRecursive( arr, 0 , len(arr)-1, 10) )

