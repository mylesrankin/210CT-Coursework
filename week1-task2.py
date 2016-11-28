import math

def countZeros(i):
    j = math.factorial(i)   # factorial of input
    j = str(j)              # turn factorial into a string to allow reversal
    count = 0               # create counter for number of zeros
    zero = True             # zero boolean for when a non zero is found
    for i in reversed(j):   # reverse number and loop from start until non zero
        if i != "0":        # if non zero is found set zero to False
            zero = False
        else:
            if zero == True: # if zero is found
                count +=1    # step up counter if zero is found
    return count            # return counter to display number of zeros found


# i.e.
# countZeros(5)
