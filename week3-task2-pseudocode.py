PRIMECHECK(n,d<-2)
    IF n = 1
        RETURN True
    ELSE IF n = d
        RETURN True
    ELSE IF (n MOD d) = 0
        return False
    ELSE
        RETURN PRIMECHECK(N,D+1)
        
