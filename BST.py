class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def insert(self, data):
    if self.root == None:
      self.root = Node(data)
    else:
      self.insertRecc(data, self.root)

  def insertRecc(self, data, current):
    if data > current.data:
      if current.right:
        self.insertRecc(data, current.right)
      else:
        current.right = Node(data)
    elif data < current.data:
      if current.left:
        self.insertRecc(data, current.left)
      else:
        current.left = Node(data)
    else:
      return "Value already exists!"

  def preorder(self):
    if self.root != None:
      self.preorderRecc(self.root)

  def preorderRecc(self, current):
    if current != None:
      print(current.data)
      self.preorderRecc(current.left)
      self.preorderRecc(current.right)

  def search(self, data):
    if self.root == None:
      return False
    else:
      return self.searchRecc(data, self.root)

  def searchRecc(self, data, current):
    if data == current.data:
      return True
    elif data > current.data:
      if current.right:
        return self.searchRecc(data, current.right)
      else:
        return False
    elif data < current.data:
      if current.left:
        return self.searchRecc(data, current.left)
      else:
        return False

    #def delete(self, data):




bst1 = BinarySearchTree()
bst1.insert(2)
bst1.insert(3)
bst1.insert(4)
bst1.insert(1)

bst1.preorder()

print(bst1.search(3))



