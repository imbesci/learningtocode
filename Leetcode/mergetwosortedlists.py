# Definition for singly-linked list.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return f'{self.data} : {self.next}'



def mergeTwoLists(l1:Node, l2:Node):
    '''
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    '''
    dummy = Node()
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        print(dummy.next)
        tail = tail.next
    
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    print(dummy.next)
    return dummy.next


l1_1 = Node(1)
l1_2 = Node(3)
l1_3 = Node(5)

l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = Node(2)
l2_2 = Node(4)
l2_3 = Node(6)

l2_1.next = l2_2
l2_2.next = l2_3

mergeTwoLists(l1_1,l2_1)