REMOVEVOWELS(n,d<-0)
    IF d = LENGTH(n)
        RETURN n
    ELSE IF LOWERCASE(n[0]) IN ["a","e","i","o","u"]
        RETURN REMOVEVOWELS(n[1:],d)
    ELSE
        RETURN REMOVEVOWELS(n[1:]+n[0],d+1)
        
