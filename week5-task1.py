class stack(): # create a standard stack class
    def __init__(self):
        self.items = []
        self.all = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def returnAll(self):
        return self.items
    def size(self):
        return len(self.items)

def selectHighest(array): # function to select highest sub sequence in 2d array
    arrayLen = 0 # set array length 0 as default
    highestSequences = [] # create a new array to handle highest sequences
    for i in array: # for each item in input array
        if len(i) > arrayLen: 
            arrayLen = len(i) # sets array length if higher than current
            highestSequences = [] # flushes current highestSequences
            highestSequences.append(i) # appends new highest sequence
        elif len(i) == arrayLen: # if two sub-s are the same size
            highestSequences.append(i) # just appends not flush if size is equal
    return(highestSequences) # returns the highest sequences
        
   
def sequences(l):
    a = []
    s = stack() # create new stack
    for i in range(0,len(l)):
        if i == (len(l)-1): # flushes stack to result when at end of sequence list 
            s.push(l[i]) # push current item to stack
            a.append(s.returnAll()) # append stack to result array (a)
        elif l[i] < l[i+1]: # if current item less than next then push to stack
            s.push(l[i]) # push item to stack
        elif l[i] > l[i+1]: # if item is more than next
            s.push(l[i]) # push item to stack
            a.append(s.returnAll()) # append stack to result array
            s = stack() # empty stack for next iteration
    return(a) # return resultant array of seperated sequences
    
# Seperate sub-sequences
# sequences([1,2,3,4,1,2,3,6,5,6,7,8])

# Seperate sub-sequences and return highest sequence(s)
# selectHighest(sequences([1,2,3,1,2,3,6,5,6,7,8]))
            
            
            
            
            
