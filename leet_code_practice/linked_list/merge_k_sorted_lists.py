from linked_list import LinkedList , Node

l = [LinkedList([1,4,5]),LinkedList([1,2,8]),LinkedList([4,6,9])]

def merge_linked_list(l):
    if not l:
        return None 
    if len(l)==1:
        return l[0].head
    val = []
    for i in l:
        current = i.head
        while current:
            val.append(current.element)
            current = current.next
    return val


def splitting(m):
    if len(m)<=1:
        return m
    mid = len(m)//2
    left = splitting(m[:mid])
    right = splitting(m[mid:])



    return merge_sort(left,right)


def merge_sort(l,r):
    i=j=0
    result = []
    while i<len(l) and j<len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1
    result.extend(l[i:])
    result.extend(r[j:])

    return result



m = merge_linked_list(l)

print(m)
p = splitting(m)

def final_merge_ll(p):
    if not p:
        return None
    head = Node(p[0])
    current = head
    for d in range(1,len(p)):
        current.next = Node(p[d])
        current = current.next

    return head


new_head = final_merge_ll(p)

ll = LinkedList()
ll.print_from_node(new_head)

