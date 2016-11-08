import math

def countZeros(i):
    j = math.factorial(i)
    j = str(j)
    count = 0
    zero = True
    for i in reversed(j):
        if i != "0":
            zero = False
        else:
            if zero == True:
                count +=1
    return count
