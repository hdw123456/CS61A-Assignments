from operator import floordiv,mod
from math import sqrt


def divide_exact(n,k):
    return floordiv(n,k),mod(n,k)


def fib(n,print_o = True):
    if n == -1:
        x = 1
    elif n == 0:
        x = 0
    else:
        x = fib(n-1,print_o) + fib(n-2,False)
    if print_o == True:
        print(x)
    return x

def has_big_sq(x):
    return x >= 0 and sqrt(x) > 10

def sum_x(n):
    """
    >>> sum_x(5)
    15
    """
    sum,i = 0,1
    while i < n + 1:
        sum = sum + i
        i += 1
    return sum

def sum_x_3(n):
    """
    >>> sum_x_3(5)
    225
    """
    sum,i = 0,1
    while i <= n:
        sum = sum + i**3
        i += 1
    return sum
    