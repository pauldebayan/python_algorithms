from queue import PriorityQueue

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



g1 = Graph()

g1.addNode('1', '2', 1)
g1.addNode('1', '3', 2)
g1.addNode('1', '4', 2)
g1.addNode('2', '3', 2)
g1.addNode('2', '4', 3)
g1.addNode('4', '3', 3)



def prims():
  pq = PriorityQueue()
  visited = {}
  ans = 0

  pq.put((0, next(iter(g1.returnAdjList()))))

  while(pq.empty() == False):
    top = pq.get()

    to = top[1]
    weight = top[0]

    if(to in visited.keys()):
      continue
    
    ans += weight
    visited[to] = True

    for ele in g1.returnAdjList()[to]:
      if ele not in visited.keys():
        pq.put((ele[1], ele[0]))
    
  print(ans)


prims()









