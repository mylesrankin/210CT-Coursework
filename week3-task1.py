'''
by @mylesrankin (github)
Reverses words in a sentence.
Example input: reverseWords("hello you") will return ("you hello")
Uses splitting then iterates from end of the split list of words
'''

def reverseWords(sentence):
    sentence = sentence.split()     # split list into words
    result = []     # create list for the reversed result
    step = -1       # start from -1 on the step as this is the end of the list
    for i in sentence: # loop through all letters
        result.append(sentence[step]) # append letters starting from the end
        step -= 1  # move step value down to select the next from the end of list

    return ' '.join(result) # join array together and return
            
            
    
