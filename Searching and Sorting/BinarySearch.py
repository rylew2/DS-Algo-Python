#https://www.geeksforgeeks.org/binary-search/



def bsIterative(arr, l, r, x):

    while l<=r:
        mid = l + (r-l)//2
        if arr[mid]==x:
            return mid
        elif x > arr[mid]:
            l = mid+1
        else:
            r= mid-1
    return -1


def bsRecursive(arr, l, r, x):

    if l <= r:
        mid = l + (r-l)//2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return bsRecursive(arr, mid+1, r, x)
        else:
            return bsRecursive(arr, l, mid-1, x)

    else:
        return -1










arr = [1,2,3,4,5]
print(bsIterative( arr, 0 , len(arr)-1, 4) )
print(bsRecursive( arr, 0 , len(arr)-1, 4) )
print('-------------------------------')
print(bsIterative( arr, 0 , len(arr)-1, 10) )
print(bsRecursive( arr, 0 , len(arr)-1, 10) )







#
# test_list = [1,3,9,11,15,19,29]
# test_val1 = 3
# test_val2 = 15
# print(binary_search(test_list, test_val1))
# print(binary_search(test_list, test_val2))



