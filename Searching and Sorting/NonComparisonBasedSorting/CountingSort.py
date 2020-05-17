# For simplicity, consider the data in the range 0 to 9.
# Input data: 1, 4, 1, 2, 7, 5, 2
#   1) Take a count array to store the count of each unique object.
#   Index:     0  1  2  3  4  5  6  7  8  9
#   Count:     0  2  2  0   1  1  0  1  0  0
#
#   2) Modify the count array such that each element at each index
#   stores the sum of previous counts.
#   Index:     0  1  2  3  4  5  6  7  8  9
#   Count:     0  2  4  4  5  6  6  7  7  7
#
# The modified count array indicates the position of each object in
# the output sequence.
#
#   3) Output each object from the input sequence followed by
#   decreasing its count by 1.
#   Process the input data: 1, 4, 1, 2, 7, 5, 2. Position of 1 is 2.
#   Put data 1 at index 2 in output. Decrease count by 1 to place
#   next data 1 at an index 1 smaller than this index.

# https://www.geeksforgeeks.org/counting-sort/


def counting_sort(arr):

    lo = min(arr) # n
    hi = max(arr) # n

    counts = [0] * (hi-lo+2) # k / k    count array should cover range (k)

    for num in arr: # n
        counts[num] += 1

    print(counts)

    for i in range(1, len(counts)): #n
        counts[i] += counts[i-1]


    print(counts)
    output = [0 for i in range(len(arr))]
    for num in arr:
        print(' {} should be at index {}'.format(num, counts[num]))
        output[counts[num]-1] = num
        counts[num] -= 1

    print(counts)
    print(output)
    return output


#offset for negative numbers
def counting_sort_neg(unsorted):
   result = [0] * len(unsorted)
   low = min(unsorted)      # we don't care if this is positive or negative any more!
   high = max(unsorted)
   count_array = [0 for i in range(low, high+1)]
   for i in unsorted:
      count_array[i-low] += 1             # use an offset index
   for j in range(1, len(count_array)):
      count_array[j] += count_array[j-1]

   print(count_array)
   for k in reversed(unsorted):
      result[count_array[k-low] - 1] = k  # here too
      count_array[k-low] -= 1             # and here
   return result


l = [1,4,1,2,7,5,2]

ans = counting_sort(l)

print( sorted(l) == ans)