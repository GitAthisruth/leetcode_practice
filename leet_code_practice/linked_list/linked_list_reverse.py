import random

head = [1,2]

class linked_list:
    def __init__(self, element):
        self.element = element
        self.next_node = None

    def setNext(self, next_node):
        self.next_node = next_node

    def getNext(self):
        return self.next_node

    def getElement(self):
        return self.element


# -----------------------------
# Create linked list
# -----------------------------
first_element = linked_list(head[0])
current = first_element

for i in head[1:]:
    new_node = linked_list(i)
    current.setNext(new_node)
    current = current.getNext()


# -----------------------------
# Print original linked list
# -----------------------------
print("Original Linked List:")
node = first_element
while node is not None:
    print(node.getElement(), end=" -> ")
    node = node.getNext()
print("None")


# -----------------------------
# Reverse linked list
# -----------------------------
prev = None
current = first_element

while current is not None:
    next_node = current.getNext()   # save next node
    current.setNext(prev)           # reverse pointer
    prev = current                  # move prev forward
    current = next_node             # move current forward

# new head of reversed list
first_element = prev


# -----------------------------
# Print reversed linked list
# -----------------------------
val = []
print("\nReversed Linked List:")
node = first_element
while node is not None:
    val.append(node.getElement())
    print(node.getElement(), end=" -> ")
    node = node.getNext()
print("None")
print("\nValues in reversed linked list:", val)





def reverseList(head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
        