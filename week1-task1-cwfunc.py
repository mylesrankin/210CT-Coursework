import random as r

def shuffle(numbers):
    newIndex = r.sample(range(len(numbers)), len(numbers))
    shuffled = []
    for j in newIndex:
        shuffled.append(numbers[j])
    return shuffled
    
