class Stack:
    def __init__(self):
        self.stack = []
    def insert(self,val):
        self.stack.append(val)
    def pop(self):
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def show(self):
        return self.stack
    def length(self):
        return len(self.stack)
    def delete_element(self,element):
        self.safe = []
        while self.top()!=element and self.length!=0:
            self.safe.append(self.pop())
        self.pop()
        while len(self.safe)!=0:
            self.insert(self.safe.pop())
        return self.show()
    
    def insert_index(self,index,element):
        self.safe = []
        iter_val =  self.length()-index
        while self.top()!=index and self.show():
            self.safe.append(self.pop())
            iter_val-=1
        self.insert(element)
        while self.safe:#length safe != 0
            self.insert(self.safe.pop())
        return index,self.show()
    


    
stack = Stack()

stack.insert(1)
stack.insert(2)
stack.insert(3)
stack.insert(4)
stack.insert(6)


print(stack.show())
stack.pop()


print(stack.show())


print(stack.delete_element(4))
print(stack.insert_index(3,4))

