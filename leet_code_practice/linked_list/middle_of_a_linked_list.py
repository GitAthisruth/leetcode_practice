from linked_list import LinkedList


list1 = LinkedList([1,2,3,4,5])

def mid_link(list1):
    l = list1.head
    ln = 0
    while l:
        l=l.next
        ln+=1
    m = ln//2
    i=0
    l = list1.head
    while i<m:
            l=l.next 
            i+=1  
    return l.element

print(mid_link(list1))


def md(list1):
    slow = list1.head
    fast = list1.head

    while fast and fast.next:
         slow = slow.next
         fast =fast.next.next
    return slow.element

print(md(list1))

