import heapq


def hq(arr, k):

    # python heapq uses a min heap
    # to find the kth largest element, we want

    z = heapq.nlargest(k, arr) # returns k largest elements in reverse sorted order





arr = [3,1,8,4,2,0,-1,10,5]