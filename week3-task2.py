import sys
sys.setrecursionlimit = 2000 # Python recursion limit very low, be wary of stack overflows
'''
Uses a step up d variable to check
all numbers below n to
see if n is divisible by them.
'''
def primeCheck(n,d=2):
    if n == 1:
        return True
    elif n == d:
        return True
    elif (n%d) == 0:
        return False
    else:
        return primeCheck(n,d+1) # Recursive 'step up' d value
    


def main(): # Check if first 50 numbers
    for i in range(1,50):
        print(i)
        print(primeCheck(i))

