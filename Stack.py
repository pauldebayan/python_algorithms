class Stack:

    def __init__(self):
        self.stack_list = []
        self.stack_len = 0
    
    def push(self, value):
        if self.stack_len == 5:
            print("Stack is Full")
        else:
            self.stack_list.append(value)
            self.stack_len += 1
    
    def pop(self):
        if self.stack_len == 0:
            print("Stack is Empty")
        else:
            peek = self.stack_list[-1]
            self.stack_list.pop(-1)
            self.stack_len -= 1
            return peek
    
    def peek(self):
        if self.stack_len == 0:
            return "No Elements Found"
        return  self.stack_list[-1]

    def isFull(self):
        if self.stack_len == 5:
            return True
        else:
            return False

    def isEmpty(self):
        if len(self.stack_list) == 0:
            return True
        else:
            return False

s1 = Stack()

s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
s1.push(6)


print(s1.isFull())

            

