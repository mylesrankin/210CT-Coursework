'''
by @mylesrankin (github)
week4-task1 binary search adaptation for finding a value between an interval
this adaptation assumes the list is sorted
IN PSEUDOCODE
'''

BINARYSEARCH(array,lower,upper)
    start <- 0
   end <- LENGTH(array)
    found <- FALSE
    WHILE (start <= end) AND (found = FALSE)
        midVal = FLOORDIVIDE((start+end),2)
        IF (array[midVal] <= UPPER) AND (array[midVal] >= lower)
            found <- TRUE
            RETURN('Value found in interval')
        ELSE
            IF lower < array[midVal]
                end <- midVal - 1
            ELSE
                start <- midVal + 1
    IF found = FALSE
        RETURN('Value could not be found in interval')


        
