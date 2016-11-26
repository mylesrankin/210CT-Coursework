ADD_MATRIX(M1,M2)
    RESULT <- EMPTY MATRIX # Imagine matrix as 2d array i.e. [[1,2][3,4]]
    FOR I IN (0 TO LEN(M1)-1)
        FOR J IN (0 TO LEN(I)-1)
            RESULT[I][J] <- M1[I][J] + M2[I][J]
    RETURN RESULT

SUB_MATRIX(M1,M2)
    RESULT <- EMPTY MATRIX # Imagine matrix as 2d array i.e. [[1,2][3,4]]
    FOR I IN (0 TO LEN(M1)-1)
        FOR J IN (0 TO LEN(I)-1)
            RESULT[I][J] <- M1[I][J] - M2[I][J]
    RETURN RESULT

MULT_MATRIX(M1,M2)
    RESULT <- EMPTY MATRIX
    FOR I IN (0 TO LEN(M1)-1 # Iterates through rows of M1
        FOR J IN (0 TO LEN(M2[0])) # Iterates through columns of M2
              FOR K IN (0 TO LEN(M2)) # Iterates through rows of M2
                  RESULT[I][J] <- M1[I][K] * M2[K][J] # row * column
    RETURN RESULT

A <- INPUT(MATRIX_A)
B <- INPUT(MATRIX_B)
C <- INPUT(MATRIX_C)

# A <- B*C+2*(B+C) to S1 = B*C, S2 = B+C, S3 = S2*2, R = S1+S3
# Split the expression into segments
S1 <- MULT_MATRIX(B,C) 
S2 <- ADD(B,C)
S3 <- ADD(S2,S2)
RESULT <- ADD(S1,S3)

PRINT(RESULT)


