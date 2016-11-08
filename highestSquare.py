def highestSquare(a):
    b = a**(1/2)
    b = b-(b%1)
    b = b*b
    return b
