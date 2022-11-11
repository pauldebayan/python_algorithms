class Queue:
    def __init__(self):
        self.queue_list = []
        self.queue_len = 0
    
    def enqueue(self, value):
        if self.isFull() == False:
            self.queue_list.append(value)
            self.queue_len += 1
    
    def dequeue(self):
        if self.isEmpty() == False:
            peek = self.queue_list[0]
            self.queue_list.pop(0)
            self.queue_len -= 1
            return peek
    
    def peek(self):
        if self.isEmpty() == False:
            return self.queue_list[0]

    def isFull(self):
        if self.queue_len == 5:
            return True
        else:
            return False

    def isEmpty(self):
        if self.queue_len == 0:
            return True
        else:
            return False

q1 = Queue()

q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)

print(q1.dequeue())

print(q1.peek())



