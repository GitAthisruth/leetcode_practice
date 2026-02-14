from linked_list import LinkedList , Node

l = [LinkedList([1,4,5]),LinkedList([1,2,8]),LinkedList([4,6,9])]


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
    
    if not val:
        return None
    sorted_vals = splitting(val) 
    return final_merge_ll(sorted_vals)



def final_merge_ll(p):
    if not p:
        return None
    head = Node(p[0])
    current = head
    for d in range(1,len(p)):
        current.next = Node(p[d])
        current = current.next

    return head


new_head = merge_linked_list(l)

ll = LinkedList()
ll.print_from_node(new_head)



hh = [3,5,6,9,1,2,3,4,5,6,1,1]

n = set()

for i in hh:
    n.add(i)

print(n)




# optimized method 




def mergeKLists(lists):
    """
    :type lists: List[Optional[ListNode]]
    :rtype: Optional[ListNode]
    """
    if not lists:
        return None

    while len(lists) > 1:
        mergedLists = []

        # Merge lists in pairs
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeTwoLists(l1, l2))

        lists = mergedLists
        print(len(lists))

    return lists[0]


def mergeTwoLists(list1, list2):
        # Get heads
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        l1 = list1.head
        l2 = list2.head

        # Dummy node
        dummy = Node(0)
        current = dummy

        # Merge process
        while l1 and l2:
            if l1.element < l2.element:
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
        print("Merged two lists:", merged_list.to_list())

        return merged_list

result = mergeKLists(l)
result.print_list()