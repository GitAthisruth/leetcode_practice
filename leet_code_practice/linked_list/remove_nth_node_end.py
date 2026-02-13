from linked_list import LinkedList 


def remove_nth_from_end(head,n):
    i = 0
    val =  head
    while val:
        val= val.next
        i+=1
    ln = i

    el= i-n
    if n==ln:
         return head.next
    current = head
    for _ in range(el-1):
       current = current.next
    current.next = current.next.next
       
    return head

head = LinkedList([1,2,3,4,5])

head.head = remove_nth_from_end(head.head,2)
head.print_list()
