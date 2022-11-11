#BellMan Ford Algorithm
class Graph:
  def __init__(self):
    self.adjList = {}

  def addNode(self, firstNode, secondNode, weight):
    if firstNode in self.adjList.keys():
      self.adjList[firstNode].extend([(secondNode, weight)])
    else:
      self.adjList[firstNode] = [(secondNode, weight)]

    # if secondNode in self.adjList.keys():
    #   self.adjList[secondNode].extend([(firstNode, weight)])
    # else:
    #   self.adjList[secondNode] = [(firstNode, weight)]

  def returnAdjList(self):
    return self.adjList


g1 = Graph()

g1.addNode('A', 'B', 6)
g1.addNode('A', 'C', 4)
g1.addNode('A', 'D', 5)
g1.addNode('C', 'B', -2)
g1.addNode('D', 'C', -2)
g1.addNode('B', 'E', -1)
g1.addNode('D', 'F', -1)
g1.addNode('C', 'E', 3)
g1.addNode('E', 'F', 3)
g1.addNode('F', 'F', 0)




def bellManFord(graph, source, destination):
  
  cost = {}
  for i in graph:
    cost[i] = float('inf')
  cost[source] = 0

  noOfRelaxation = len(graph) - 1

  while noOfRelaxation:

    for elem in graph:
      for elems in graph[elem]:
        costCal = cost[elem]+elems[1]
        if costCal < cost[elems[0]]:
          cost[elems[0]] = costCal

    noOfRelaxation -= 1


  return cost[destination]

print(bellManFord(g1.returnAdjList(), 'A', 'E'))
#print(g1.returnAdjList())









