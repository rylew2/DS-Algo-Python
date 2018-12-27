"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""



#input_array - Python list to search through
#value - the value you're searching for
def binary_search(input_array, value):
    """Your code goes here."""
    low = 0
    high = len(input_array) -1
    while( low <= high):
        mid = int((low+high)/2)  #int() will round down ==>  int(7/2)=3
        if value==input_array[mid]:
            return mid
        elif value > input_array[mid]:
            low = mid + 1
        else:
            high = mid-1

    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))