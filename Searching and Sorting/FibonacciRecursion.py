"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

from functools import lru_cache

# Fibonacci sequence: 0,1,1,2,3,5,8,13,21,34..

# Memoization - cache results of prior function calls so we don't have to repeat fib(1), fib(2) etc...

fibonacci_cache = {} #explicit way to memoize


# @lru_cache(maxsize=1000) # simple way to memoize
def get_fib(position):
    if type(position) != int or position < 0:
        raise TypeError('n must be a positive int')

    #if we have cached the value, return it
    if position in fibonacci_cache:
        return fibonacci_cache[position]

    #compute the Nth term
    if position == 0 or position == 1:
        return position
    value =  get_fib(position - 1) + get_fib(position - 2)
    fibonacci_cache[position] = value
    return value

# Test cases
# print(get_fib(-1))
# print(get_fib("one"))

for n in range(1,200):
    print(get_fib(n))
