class LinkedlistNode:
    def __init__(self,elements):
        self.elements = elements
        self.next = None
    def set_next(self,next_node):
        self.next = next_node
    def get_next(self):
        return self.next
    def get_elements(self):
        return self.elements
    
