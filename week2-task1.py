'''
by @mylesrankin (github)
Finds highest square by rooting input, rounding to a whole number
then squaring to find the highest square up to the input number
'''

def highestSquare(a):
    if a >= 0:
      b = a**(1/2) # root input
      b = b-(b%1)  # take away remainder
      return int(b*b)      # square to get highest perfect square
    else:
      return("Enter a number that is greater than zero")
