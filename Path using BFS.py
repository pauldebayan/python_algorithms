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


def bfs(graph, node):

    visited, queue = [], []
    dist = {}


    dist[node] = 0

    parent = {}

    visited.append(node)
    queue.append(node)

    while queue:
        current = queue.pop(0)
        print(current, end=' ')
        for neighbour in graph[current]:

            if neighbour in parent.keys():
                parent[neighbour].append(current)
            else:
                parent[neighbour] = [current] 

            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

                dist[neighbour] = dist[current] + 1
    
    print(dist)
    print(parent)

    visitedDest = {}

    def path(source, dest):
        if source == dest:
            return True
        visitedDest[dest] = True

        if dest not in parent.keys():
            return False

        for allParent in parent[dest]:
            if allParent not in visitedDest.keys():
                if(path(source, allParent)):
                    print(allParent, end='--> ')
                    return True

        return False

    if path(0, 10):
        print(6, end='')
    else:
        print("Path Doesn't Exist!")





g1 = Graph()

g1.addNode(1, 2)
g1.addNode(1, 0)
g1.addNode(2, 3)
g1.addNode(3, 4)
g1.addNode(3, 5)
g1.addNode(0, 4)
g1.addNode(4, 5)
g1.addNode(5, 6)

bfs(g1.returnAdjList(), 2)
