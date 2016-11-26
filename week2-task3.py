
ADD_MATRIX(M1,M2)
    RESULT = EMPTY MATRIX # Imagine matrix as 2d array i.e. [[1,2][3,4]]
    FOR I IN M1
        FOR J IN I
            RESULT[I][J] = M1[I][J] + M2[I][J]
        

SUB_MATRIX(M1,M2)
    RESULT = EMPTY MATRIX # Imagine matrix as 2d array i.e. [[1,2][3,4]]
    FOR I IN LEN(M1)
        FOR J IN LEN(I)
            RESULT[I][J] = M1[I][J] - M2[I][J]

MULT_MATRIX(M1,M2)
    
    

A <- INSERT(MATRIX_A)
B <- INSERT(MATRIX_B)
C <- INSERT(MATRIX_C)

A <- B*C+2*(B+C)

# Split the expression into segments
S1 <- MULT_MATRIX(B,C) 
S2 <- ADD(B,C)
S3 <- ADD(S2,S2)
RESULT = ADD(S1,S3)

PRINT(RESULT)


