

def bucketsort(x):
    arr = [] #store buckets as list of lists
    buckets = len(x)

    # create len(x) empty buckets
    for i in range(buckets):
        arr.append([])

    #put in appropriate buckets
    for j in x:
        bucketNum = int(j*buckets) #round down
        arr[bucketNum].append(j)

    for i in range(len(arr)):
        if len(arr[i])>=2:
            arr[i].sort()

    k=0
    for i in range(buckets):
        if arr[i]!=None:
            for j in range(len(arr[i])):
                x[k] = arr[i][j]
                k+=1
    return x





# alist = [4,3,2,1]
l = [.08, .07, .39, .26, .72, .94, .21, .12, .23, .68]
bucketsort(l)
print(l)
