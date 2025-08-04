#task 1
def factorial(n):
    if n <2 :
        return 1
    else:
        return n*(factorial(n-1))
n = int(input('enter the number:'))
result = factorial(n)
print('factorial of n is:',result)


# task
from math import *
num= int(input('enter the number'))
sqr= sqrt(num)
log = log(num,e)
sine= sin(num)
print('square root:',sqr)
print('logarithm:',log)
print('sine:',sine)

