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
            highestSequences.append(i)
        elif len(i) == arrayLen:
            break
   
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
    
            
    print("list:" , a)
            
            
            
            
            
