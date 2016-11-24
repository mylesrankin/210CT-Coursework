class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class Graph(object):
    def __init__(self):
        self.graphDict = {}

    def addVertex(self,label):
        if label not in self.graphDict:
            self.graphDict[label] = []
            return("Vertex created")
        else:
            return("Vertex exists")

    def addEdge(self,vertex1,vertex2):
        self.graphDict[vertex1].append(vertex2)
        self.graphDict[vertex2].append(vertex1)
        return("An edge has been created between",vertex1," and ",vertex2)

    def displayGraph(self):
        return self.graphDict

    def displayAdjacencyList(self):
        for k,v in self.graphDict.items():
            print(k , "|", v)

    def depthFirstSearch(self,startNode):
        s = Stack()
        visited = []
        s.push(startNode)
        while s.isEmpty() == False:
            u = s.pop()
            if u not in visited:
                visited.append(u)
                for e in self.graphDict[u]:
                    s.push(e)
        return visited
                

if __name__ == "__main__":
    g = Graph()
    g.addVertex("a")
    g.addVertex("b")
    g.addVertex("c")
    g.addEdge("a","b")
    g.addEdge("a","c")
    g.displayAdjacencyList()
    print(g.depthFirstSearch("a"))
