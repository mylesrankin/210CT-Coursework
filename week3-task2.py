import sys
sys.setrecursionlimit = 2000 # Python recursion limit very low, be wary of stack overflows
'''
Myles Rankin 2016
Uses a step up d variable to check
all numbers below n to
see if n is divisible by them.
'''
def primeCheck(n,d=2):
    if n == 1: # 1 is always a prime number
        return True
    elif n == d: # if step value equals d then all numbers to n have been checked
        return True
    elif (n%d) == 0: # n%d=0 implies n is div by another number so not prime
        return False
    else:
        return primeCheck(n,d+1) # Recursive 'step up' d value to n
    

# Example of checking first 50 prime numbers
for i in range(1,50):
    print(i)
    print(primeCheck(i))

