from linked_list import Linked


def splitt(link):
    mid = (link.length() // 2)-1
    mid_value = link.index(mid)

    left = link
    right = Linked()
    right.head = mid_value.next
    mid_value.next = None
    return left, right

def merge(l, r):
    left = l.head
    right = r.head
    new_linked = Linked()
    new_linked.add("fake",0,"fake","fake")
    temp = new_linked.head

    while left or right:
        if left is None:
            temp.next = right
            right = right.next
        elif right is None:
            temp.next = left
            left = left.next
        else:
            if left.name.lower() < right.name.lower():
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
        temp = temp.next
    head = new_linked.head.next
    new_linked.head = head
    return new_linked

def linkedList_MergeSort(link):
    if link is None or link.length() == 1:
        return link
    left , right = splitt(link)
    l = linkedList_MergeSort(left)
    r = linkedList_MergeSort(right)
    return merge(l, r)



