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



class Solution:
    def mergeTwoLists(self, list1, list2):
        # Get heads
        l1 = list1.head
        l2 = list2.head

        # Dummy node
        dummy = Node(0)
        current = dummy

        # Merge process
        while l1 and l2:
            if l1.element <= l2.element:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Attach remaining nodes
        if l1:
            current.next = l1
        else:
            current.next = l2

        # Return as LinkedList
        merged_list = LinkedList()
        merged_list.head = dummy.next

        return merged_list

list1 = LinkedList([1, 3, 5])
list2 = LinkedList([2, 4, 6])

sol = Solution()
merged = sol.mergeTwoLists(list1, list2)

merged.print_list()