from linked_list import LinkedList

# head = LinkedList([1,2,3,4])

def reorder(head):

    val = head
    while val:
        print(val.element , end = " -> ")
        val = val.next

    print("\n")

    prev = None
    current = head
    while current:
        new_node = current.next
        current.next = prev
        prev = current
        current = new_node

    return prev
    

# head = LinkedList([1,2,3,4,5]) 
# head.head = reorder(head.head)
# head.print_list()



def mid(head):
    if not head or not head.next:
        return None

    # Step 1: Find middle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Split list
    second_half = slow.next
    slow.next = None

    # Step 3: Reverse second half
    prev = None
    current = second_half

    while current:
        nextnode = current.next
        current.next = prev
        prev = current
        current = nextnode

    # prev = head of reversed second half

    first = head
    second = prev
    while second:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2 

    return head



head1 = LinkedList([1,2,3,4,5])
head1.print_list()

rever = mid(head1.head)   

print("First half:")
head1.print_list()

print("Reversed second half:")
head1.print_from_node(rever)

