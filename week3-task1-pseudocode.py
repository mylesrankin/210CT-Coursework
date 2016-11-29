REVERSEWORDS(sentence)
    sentence <- SPLIT(sentence)
    result <- NEW ARRAY
    step <- -1
    FOR I IN SENTENCE
        APPEND TO RESULT(sentence[step])
        step <- step - 1
    RETURN JOIN(result)
