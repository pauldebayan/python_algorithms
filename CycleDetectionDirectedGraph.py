class Graph:
  def __init__(self):
    self.adjList = {}

  def addNode(self, firstNode, secondNode):
    if firstNode in self.adjList.keys():
      self.adjList[firstNode].append(secondNode)
    else:
      self.adjList[firstNode] = [secondNode]
    if secondNode not in self.adjList.keys():
        self.adjList[secondNode] = []

  def printList(self):
    print(self.adjList)

  def returnAdjList(self):
    return self.adjList


visited = set()
stk=[]
def dfs(graph, node):
    print(stk)
    if node not in visited:
        visited.add(node)
        print(node, end=' ')
        for neighbour in graph[node]:
          if neighbour in stk:
            print("Cycle Present")
          stk.append(neighbour)
          dfs(graph, neighbour)
          stk.pop(-1)

g1 = Graph()

g1.addNode(1, 2)
g1.addNode(2, 3)
g1.addNode(3, 0)
g1.addNode(0, 1)
g1.addNode(0, 4)
g1.addNode(0, 5)
g1.addNode(5, 4)

g1.printList()

for i, ele in enumerate(reversed(g1.returnAdjList().keys())):
  stk.clear()
  stk.append(ele)
  if ele not in visited:
    dfs(g1.returnAdjList(), ele)
