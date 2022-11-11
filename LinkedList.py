class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
  
class LinkedList:
  def __init__(self):
    self.head = None

  def insertFirst(self, data):
    newNode = Node(data)
    if(self.head):
      newNode.next = self.head
    self.head = newNode

  def insertLast(self, data):
    newNode = Node(data)
    
    if self.head:
      current = self.head
      while current.next:
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

  def insertNth(self, data, n):
    if n == 0:
      self.insertFirst(data)
    else:
      n -= 1
      newNode = Node(data)
      current = self.head
      while n:
        current = current.next
        n -= 1
      newNode.next = current.next
      current.next = newNode
      
  def deleteFirst(self):
    if(self.head):
      current = self.head
      self.head = current.next
    else:
      self.head = None

  def printLL(self):
    current = self.head
    while current.next:
      print(current.data, end=' ')
      current = current.next
    print(current.data, end=' ')

l1 = LinkedList()
l1.insertLast(2)
l1.insertLast(4)
l1.insertLast(6)
l1.insertLast(8)
l1.deleteFirst()
l1.insertNth(5,2)

l1.printLL()


