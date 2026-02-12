from linked_list import LinkedList 


def remove_nth_from_end(head):
    prev = None
    current = head
    while current:
        new_node = current.next
        current.next = prev
        prev = current 
        current = new_node
    return prev




head = LinkedList([1,2,3,4,5])

head.head = remove_nth_from_end(head.head)
head.print_list()
