'''import math
a=int(input())
b=int(input())
GCD=math.gcd(a,b)'''


'''def sum_of_N1(n):
    if n==0:
        return 0
    return n+sum_of_N1(n-1)
print(sum_of_N1(5))
print(sum_of_N1(10))
'''

#factorial of the number
'''
def factorial(n):
    if n<0:
        return "no factorial -ves"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
print(factorial(-8))
'''
#fibonacci
'''
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))
'''
#GCD of two numbers:
'''
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(4,10))
'''