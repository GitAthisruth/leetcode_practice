# Linked_list

# Basic building block is a node which contains data and a pointer to the next node(that is a memory reference to the next node) in a sequence.

# 1.Data (Value) → The actual information stored (e.g., a number, string, or object).

# 2.Pointer (Next) → A reference to the next node in the list (or null / None if it’s the last node).


# import random

# class LinkedList:
#     def __init__(self,element):
#         self.element=element
#         self.nextNode=None
#     def setNext(self,nextNode):
#         self.nextNode = nextNode
#     def getNext(self):
#         return self.nextNode
#     def getElement(self):
#         return self.element
    
# element = LinkedList(10)
# next_node = element

# for i in range(10):
#     print(f"Adding element {i}")
#     random_elem = random.randint(1,100)
#     new_node = LinkedList(random_elem)
#     next_node.setNext(new_node)
#     next_node = next_node.getNext()


# next_node = element
# count = 0
# while element is not None:
#     print(element.getElement())
#     count+=1
#     element = element.getNext()

# print(f"len of the linked_list is:{count}")



# def detect_cycle(head):
#     slow = head
#     fast = head

#     while fast is not None and fast.getNext() is not None:
#         slow = slow.getNext()
#         fast = fast.getNext().getNext()
#         if slow == fast:
#             return True
#     return False

# # Example usage:
# print("Has cycle?", detect_cycle(element))


# Find the length of a linked list

# Question:
# Write a function that takes the head node of a linked list and returns the number of nodes in it.



# class Node:
#     def __init__(self, element):
#         self.element = element
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None  # start of the list

#     def add_at_end(self, element):
#         new_node = Node(element)
#         if self.head is None:        # if list is empty
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:      # go to the end
#                 current = current.next
#             current.next = new_node  # add new node at end

#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.element, end=" -> ")
#             current = current.next
#         print("None")



#stack

# class Stack:
#     def __init__(self):
#         self.stack = []
#     def insert(self,element):
#         self.stack.append(element)
#     def pop(self):
#         self.stack.pop()
#     def top(self):
#         return self.stack[-1]
#     def show_the_stack(self):
#         return self.stack
#     def length(self):
#         return len(self.stack)
#     def delete(self,element):
#         self.safe = []

#         while self.top()!=element and self.length!=0:
#             self.safe.append(self.stack.pop())
#         if self.length!=0:
#             self.pop()
#         while len(self.safe)!=0:
#             self.insert(self.safe.pop())
        
#         print(f"Stack:{self.show_the_stack()} after deleting the :{element} ")


#     def insert_to_index(self,target_index,element):
#         self.safe = []
#         target_iter =  self.length() - target_index
#         while target_iter>0:
#             print(f"stack after pop :{self.stack} and safe after append:{self.safe}")
#             self.safe.append(self.stack.pop())
#             target_iter-=1
#         self.insert(element)

#         while len(self.safe)!=0:
#             self.insert(self.safe.pop())
#         print(f"final stack: {self.show_the_stack()} after inserting element :{element} to the given index: {target_index}")



# stack = Stack()
# stack.insert(5)
# stack.insert(8)
# stack.insert(20)
# stack.insert(35)
# stack.insert(12)

# # stack.delete(5)
# stack.insert_to_index(4,90)



# Queue


# class Queue:
#     def __init__(self):
#         self.queue = []
#     def enqueue(self,value):
#         self.queue.append(value)
#     def dequeue(self):
#         if not self.queue:
#             return None
#         else:
#             self.queue.pop(0)
#     def  delete(self,value):
#         self.safe = []
#         for i in self.queue:
#             if i != value:
#                 self.safe.append(i)
#             else:
#                 print("the given value deleted")
#         self.queue = self.safe
#     def print_queue(self):
#         return self.queue
    


# queue = Queue()

# queue.enqueue(10)
# queue.enqueue(11)
# queue.enqueue(12)
# queue.enqueue(13)
# queue.enqueue(14)
# queue.enqueue(15)

# queue.dequeue()
# queue.delete(11)
# print(queue.print_queue())






#Binary Search in Tree



# arr = [1, 4, 7, 10, 12, 15, 20, 24, 30,1,59]

# arr.sort()
# print(arr)
# x = 20

# start = 0

# end = len(arr) -1

# sf = 0

# while start<=end:
#     mid = (start+end)//2
#     if arr[mid]==x:
#         sf =1
#         print(f"success_flag:{sf} and index of {x} is {mid}")
#         exit()
#     elif arr[mid] <x:
#         start = mid+1
#     else:
#         end = mid-1
    




#Tree
