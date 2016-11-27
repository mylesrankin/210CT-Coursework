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

class Queue:
     def __init__(self):
          self.items = []

     def isEmpty(self):
          return self.items == []

     def enqueue(self, item):
          self.items.insert(0,item)

     def dequeue(self):
          return self.items.pop()

     def size(self):
          return len(self.items)

class Graph:
     def __init__(self):
        self.graphDict = {}

     def addVertex(self,label):
          if label not in self.graphDict:
               self.graphDict[label] = []
               return("Vertex created")
          else:
                 return("Vertex exists")

     def addEdge(self,vertex1,vertex2,weight):
          edge1 = dict({vertex2: weight})
          edge2 = dict({vertex1: weight})
          self.graphDict[vertex1].append(edge1)
          self.graphDict[vertex2].append(edge2)
          return("An edge has been created between",vertex1," and ",vertex2)

     def displayGraph(self):
          return self.graphDict

     def displayAdjacencyList(self):
          for k,v in self.graphDict.items():
               print(k , "|", v)

     def dijkstra(start,end):
          

if __name__ == "__main__":
    g = Graph()
    g.addVertex("a")
    g.addVertex("b")
    g.addVertex("c")
    g.addVertex("d")
    g.addVertex("e")
    g.addEdge("a","b",2)
    g.addEdge("a","e",3)
    g.addEdge("a","c",5)
    g.addEdge("b","e",7)
    g.addEdge("b","d",1)
    g.displayAdjacencyList()
