from linked_list import LinkedList

l1 = LinkedList([1,2,3,4,5,3])



def l_c(l1):
    slow = l1.head
    fast = l1.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False 

print(l_c(l1))