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

  def returnAdjList(self):
    return self.adjList


g1 = Graph()

g1.addNode(1,2)
g1.addNode(2,3)
g1.addNode(3,4)
g1.addNode(4,1)


def checkCycleUsingDSU() -> bool:

    parent = [-1]*(len(g1.returnAdjList())+1)
    rank = [1]*(len(g1.returnAdjList())+1)

    def find(i):
      if parent[i] == -1:
        return i
      else:
        return find(parent[i])

    def union(i, j):
      s1 = find(i)
      s2 = find(j)

      if s1 != s2:
        #parent[s2] = s1
        if(rank[s1] < rank[s2]):
          parent[s1] = s2
          rank[s2] += rank[s1]
        else:
          parent[s2] = s1
          rank[s1] = rank[s2]

      else:
        return True

    for ele in g1.returnAdjList():
      for edg in g1.returnAdjList()[ele]:
        if(union(ele, edg)):
          return True
  
if(checkCycleUsingDSU()):
  print("Graph contains Cycle")
else:
  print("Graph does not contain Cycle")
