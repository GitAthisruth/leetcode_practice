class Node:
    def __init__(self, element):
        self.element = element
        self.next = None


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            self.create(values)

    def create(self, values):
        self.head = Node(values[0])
        current = self.head
        for val in values[1:]:
            current.next = Node(val)
            current = current.next

    def print_list(self):
        node = self.head
        while node:
            print(node.element, end=" -> ")
            node = node.next
        print("None")


    def print_from_node(self,node):
        while node:
            print(node.element, end=" -> ")
            node = node.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def to_list(self):
        result = []
        node = self.head
        while node:
            result.append(node.element)
            node = node.next
        return result


