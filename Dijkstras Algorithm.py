#https://www.youtube.com/watch?v=pVfj6mxhdMw
class Graph:
  def __init__(self):
    self.adjList = {}

  def addNode(self, firstNode, secondNode, weight):
    if firstNode in self.adjList.keys():
      self.adjList[firstNode].extend([(secondNode, weight)])
    else:
      self.adjList[firstNode] = [(secondNode, weight)]

    if secondNode in self.adjList.keys():
      self.adjList[secondNode].extend([(firstNode, weight)])
    else:
      self.adjList[secondNode] = [(firstNode, weight)]

  def returnAdjList(self):
    return self.adjList


g1 = Graph()

g1.addNode('A', 'B', 1)
g1.addNode('A', 'C', 5)
g1.addNode('B', 'C', 2)
g1.addNode('B', 'D', 7)
g1.addNode('C', 'D', 1)

def dijkstra(graph, source, destination):
  cost = {}
  for i in graph:
    cost[i] = float('inf')
  cost[source] = 0

  visited=[]
  unvisited={source: 0}

  while unvisited:
    minUnvisited = min(unvisited, key=unvisited.get)
    del unvisited[minUnvisited]

    if minUnvisited not in visited:
      
      for neighbour in graph[minUnvisited]:
        if neighbour[0] not in visited:
          costCal = cost[minUnvisited]+neighbour[1]
          if costCal < cost[neighbour[0]]:
            cost[neighbour[0]] = costCal
            unvisited[neighbour[0]] = costCal

      visited.append(minUnvisited)

  return cost[destination]

print(dijkstra(g1.returnAdjList(), 'A', 'D'))
#print(g1.returnAdjList())









