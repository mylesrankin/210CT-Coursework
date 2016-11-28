import sys, math
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
               self.graphDict[label] = {}
               return("Vertex created")
          else:
                 return("Vertex exists")

     def addEdge(self,vertex1,vertex2,weight):
          edge1 = dict({vertex2: weight})
          edge2 = dict({vertex1: weight})
          self.graphDict[vertex1].update(edge1)
          self.graphDict[vertex2].update(edge2)
          return("An edge has been created between",vertex1," and ",vertex2)

     def displayGraph(self):
          return self.graphDict

     def displayAdjacencyList(self):
          for k,v in self.graphDict.items():
               print(k , "|", v)

     def dijkstra(self,start,end): # start = source node, end = destination, distances = tentative weights
          distances={}
          visited = []
          previous = []
          v = start
          for n in g.graphDict:
               distances[n] = math.inf
          distances[start] = math.inf
          while v != end:
               for k in self.graphDict[v]: # k,w for key : weight in graphDict[v]
                    if distances[v]+self.graphDict[v][k] < distances[k]:
                         distances[k] = distances[v]+self.graphDict[v][k]
                         previous[v] = 
               print(visited)
               visited.append(v)
               _min = math.inf
               for n in self.graphDict[v]:
                    if (n not in visited) and (distances[n] < _min):
                         v = n
                         _min = distances[n]
          return visited
               

     def shortestpath(self,start,end,visited=[],distances={},predecessors={}):
    # we've found our end node, now find the path to it, and return
         if start==end:
             path=[]
             while end != None:
                 path.append(end)
                 end=predecessors.get(end,None)
             return distances[start], path[::-1]
    # detect if it's the first time through, set current distance to zero
         if not visited: distances[start]=0
    # process neighbors as per algorithm, keep track of predecessors
         for neighbor in self.graphDict[start]:
             if neighbor not in visited:
                 neighbordist = distances.get(neighbor,sys.maxsize)
                 tentativedist = distances[start] + self.graphDict[start][neighbor]
                 if tentativedist < neighbordist:
                     distances[neighbor] = tentativedist
                     predecessors[neighbor]=start
    # neighbors processed, now mark the current node as visited
         visited.append(start)
    # finds the closest unvisited node to the start
         unvisiteds = dict((k, distances.get(k,sys.maxsize)) for k in self.graphDict if k not in visited)
         closestnode = min(unvisiteds, key=unvisiteds.get)
    # now we can take the closest node and recurse, making it current
         return self.shortestpath(closestnode,end,visited,distances,predecessors)

     

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
