from linked_list import LinkedList,Node

head = LinkedList([1,1,9,9])

def add_one_to_ll(head):
    if not head:
        return None
    val = []

    current = head
    while current:
        val.append(str(current.element))
        current = current.next

    val = int("".join(val))+1

    val = list(map(int,str(val)))

    new_head = Node(val[0])
    current = new_head

    for i in range(1,len(val)):
        current.next = Node(val[i])
        current = current.next
    return new_head


val = add_one_to_ll(head.head)
head.print_from_node(val)