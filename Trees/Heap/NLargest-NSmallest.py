from heapq import heapify, heappushpop, nlargest, nsmallest


def my_nlargest(arr, k):
    kheap = arr[:k]
    heapify(kheap)
    for j in range(k, len(arr)):
        heappushpop(kheap, arr[j])
    kheap.sort()

    return kheap[0]

def my_nsmallest(arr, k):
    for j in range(len(arr)):
        arr[j] *= -1

    negkheap = my_nlargest(arr,k)
    for j in range(len(arr)):
        arr[j] *= -1
    return negkheap * -1


l = [4,1,6,8,2,10,15,3,6]
k = 2

print(my_nlargest(l, k))
print(my_nsmallest(l, k))

print(nlargest(k, l)[-1] == my_nlargest(l, k))
print(nsmallest(k, l)[-1] == my_nsmallest(l, k))









