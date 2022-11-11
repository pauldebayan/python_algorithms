#bfs

class Graph:
  def __init__(self):
    self.adjList = {}

  def addNode(self, firstNode, secondNode):
    if firstNode in self.adjList.keys():
      self.adjList[firstNode].append(secondNode)
    else:
      self.adjList[firstNode] = [secondNode]
    if secondNode in self.adjList.keys():
      self.adjList[secondNode].append(firstNode)
    else:
      self.adjList[secondNode] = [firstNode]
    


  def printList(self):
    print(self.adjList)

  def returnAdjList(self):
    return self.adjList

visited = []
queue = []

def bfs(graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    current = queue.pop(0)
    print(current, end=' ')
    for neighbour in graph[current]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)




g1 = Graph()

g1.addNode('A', 'B')
g1.addNode('A', 'D')
g1.addNode('B', 'C')
#g1.addNode('C', 'D')
g1.addNode('C', 'E')
g1.addNode('D', 'E')

#g1.printList()

bfs(g1.returnAdjList(), 'A')







