#Building stack using queue .

class MyStack(object):

    def __init__(self):
        self.stack = []
        self.stack_d =[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.stack:
            while len(self.stack)!=1:
                self.stack_d.append(self.stack.pop(0))
            pop = self.stack.pop(0)
            self.stack = self.stack_d
            self.stack_d = []
            return pop
        else:
            return 

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            while len(self.stack)!=1:
                self.stack_d.append(self.stack.pop(0))
            top = self.stack[0]
            self.stack = self.stack_d + self.stack
            self.stack_d = [] 
            return top
        else:
            return

        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.stack:
            return True
        else:
            return False

    def show(self):
        return self.stack    
     
obj = MyStack()
obj.push(2)
obj.push(3)
obj.push(4)
# print(obj.show())
print(obj.pop())
# print(obj.top())
# print(obj.empty())


