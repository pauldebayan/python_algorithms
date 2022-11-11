#dfs

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


visited = set()
def dfs(graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour)

g1 = Graph()

g1.addNode('A', 'B')
g1.addNode('A', 'D')
g1.addNode('B', 'C')
#g1.addNode('C', 'D')
g1.addNode('C', 'E')
g1.addNode('D', 'E')

#g1.printList()

dfs(g1.returnAdjList(), 'A')






