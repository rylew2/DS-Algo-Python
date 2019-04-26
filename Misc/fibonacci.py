

# Time => 2^n , Space=> N
def fibRecursive(n):
    if n==0 or n==1: return n
    else:
        return fibRecursive(n-1) + fibRecursive(n-2)

# Time => N , Space=> N
def fibRecursiveMemo(a, cache={0:0,1:1}):
    if a in cache: return cache[a]
    res = fibRecursiveMemo(a-1, cache) + fibRecursiveMemo(a-2, cache)
    cache[a] = res
    return res

# Time => N , Space=> 1
def fibIterative(n):
    if n==0 or n==1: return n
    a=0; b=1;
    for i in range(2, n+1):
        c = a+b
        a=b
        b=c
    return b

def fibFormula(n):
    import math
    phi = ((1+math.sqrt(5))/2)
    return  round((phi**n) / math.sqrt(5))

print (fibFormula(5))
print('===============')


print(fibRecursive(2))
print(fibRecursive(3))
print(fibRecursive(4))
print(fibRecursive(5))
print('======================')
print(fibRecursive(2))
print(fibRecursive(3))
print(fibRecursive(4))
print(fibRecursive(5))

print('==================')
print(fibRecursiveMemo(2))
print(fibRecursiveMemo(3))
print(fibRecursiveMemo(4))
print(fibRecursiveMemo(5))

