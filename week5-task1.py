class stack():
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

def selectHighest(array):
    arrayLen = 0
    highestSequences = []
    for i in array:
        if len(i) > arrayLen:
            arrayLen = len(i)
            highestSequences = []
            highestSequences.append(i)
        elif len(i) == arrayLen: # if two sub-s are the same size
            highestSequences.append(i)
    return(highestSequences)
        
   
def sequences(l):
    a = []
    s = stack()
    for i in range(0,len(l)):
        if i == (len(l)-1):
            s.push(l[i])
            a.append(s.returnAll())
        elif l[i] < l[i+1]:
            s.push(l[i])
        elif l[i] > l[i+1]:
            s.push(l[i])
            a.append(s.returnAll())
            s = stack()
    return(a)
    
# Seperate sub-sequences
sequences([1,2,3,4,1,2,3,6,5,6,7,8])

# Seperate sub-sequences and return highest sequence(s)
selectHighest(sequences([1,2,3,4,1,2,3,6,5,6,7,8]))
            
            
            
            
            
