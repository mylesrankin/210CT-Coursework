'''
by @mylesrankin (github)
week4-task1 binary search adaptation for finding a value between an interval
this adaptation assumes the list is sorted
'''
def binarySearch(l,lower,upper):        
    start,end = 0,len(l)-1                      # start and end values of the list
    found = False                               # set found as false
    while start <= end and not found:           # whilst start is less than end, and found isn't true loop through binary search
        midVal = (start+end)//2                 # Finds midpoint with a floor div (//)
        if (l[midVal] <= upper) and (l[midVal] >= lower) :  # Checks value is between the interval provided
            found = True                        # set found as True because value is within interval
            return True
        else:
            if (lower < l[midVal]):             # if the middle value is less than lower interval   
                end = midVal-1                  # ...change the end interval to one less than midval, so reducing the binary search half
            else:
                start = midVal+1                # same as above but for the lower half is being removed
    if found == False:                          # when found is false return False (value not found in interval)
        return False

# example binarySearch([2,3,5,7,9,13],10,14) will yield True


                
    
    
    
