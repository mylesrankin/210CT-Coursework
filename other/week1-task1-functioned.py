'''
by @mylesrankin (github)
Shuffles an array of numbers randomly by using a random sample of the indexes
to then create a new list using those indexes.
'''

import random as r

def shuffle(numbers):
    newIndex = r.sample(range(len(numbers)), len(numbers)) # Creates new indexes using sample
    shuffled = [] # Create a new array for shuffled result
    for j in newIndex:
        shuffled.append(numbers[j]) # Inserts into new indexes
    return shuffled
    
# Example run
# shuffleArray([5,3,8,6,1,9,2,7])
