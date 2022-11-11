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
    


  def printList(self):
    print(self.adjList)

  def returnAdjList(self):
    return self.adjList


visited = []
def dfs(graph,node):
  if node not in visited:
    visited.append(node)
    print(node, end='')

    for neighbour in graph[node]:
      if neighbour[0] not in visited:
        dfs(graph, neighbour[0])


g1 = Graph()

g1.addNode('A', 'B', 6)
g1.addNode('A', 'D', 5)
g1.addNode('B', 'C', 7)
#g1.addNode('C', 'D', 8)
g1.addNode('C', 'E', 10)
g1.addNode('D', 'E', 9)

#g1.printList()

dfs(g1.returnAdjList(), 'A')









