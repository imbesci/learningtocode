class node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        string  = ''
        start = self
        while self != None:
            string += (str(self.val) + ' ')
            self = self.next
        return string

a = node(1)
b = node(2)
c = node(3)
d = node(4)
e = node(5)
f = node(6)

a.next = b
b.next= c
c.next = d
d.next = e
e.next = f

w = node(10)
x = node(11)
y = node(12)
z = node(13)

w.next = x
x.next = y
y.next = z

# A -> B -> C -> D -> None

########### PRINT A LINKED LIST ##################

# def printLinkedList(head:node):
#     current = head
#     while current != None:
#         print(current.val)
#         current = current.next

# def printRecursive(head):
#     if head == None:
#         return

#     print(head.val)
#     printRecursive(head.next)

########### PUT VALUES OF A LINKED LIST INTO AN ARRAY ##################

# def arrayList(head:node):
#     arr = []
#     current = head
#     while current != None:
#         arr.append(current.val)
#         current = current.next
#     return arr

# def fillValues(head, arr):
#     if head == None:
#         return
#     arr.append(head.val)
#     fillValues(head.next, arr)

# def recursiveArrayList(head:node) -> list:
#     arr = []
#     fillValues(head, arr)
#     return arr

########### SUM THE VALUES OF A NUMERICAL LINKED LIST ##################

# def sumList(head:node) -> int:
#     total = 0
#     index = 0
#     current = head
#     while current != None:
#         total += current.val
#         index += 1
#         current = current.next
#     else:
#         print(f'Node at index {index} has value: None')
#         return total
    
# def sumRecursively(head:node):
#     if head == None:
#         return 0
#     return head.val + sumRecursively(head.next)

########### CHECK IF A CERTAIN VALUE IS IN OUR LINKED LIST  ##################
# def inList(head:node, target) -> bool:
#     cur = head
#     while cur != None:
#         if cur.val == target:
#             return True
#         cur = cur.next
#     return False

# def inListR(head:node, target):
#     if head == None:
#         return False
#     elif head.val == target:
#         return True
#     else:
#         return inListR(head.next, target)

########### GET THE VALUE AT A CERTAIN INDEX ##################
# def valueAtIndex(head:node, tgtIndex):
#     index = 0
#     current = head
#     while index < tgtIndex:
#         if current == None:
#             raise IndexError
#         index += 1
#         current = current.next
#     return current.val

# def valRecursive(head:node, index):
#     if head == None: return IndexError('Index out of range')
#     elif 0 == index:
#         return head.val
#     else:
#         return valRecursive(head.next, index-1)

########### REVERSE A LINKED LIST ##################

def reverseList(head:node):
    current = head
    prev = None
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

# def recursiveReverse(head:node, prev = None):
#     if head == None:
#         return prev
#     else:
#         next = head.next
#         head.next = prev
#         prev = head
#         return recursiveReverse(next,prev)

########### MERGE A LINKED LIST STARTING WITH L1  ##################
# def mergeLists(l1:node, l2:node):
#     dummy = node(None)
#     tail = dummy
#     alternator = False
#     while l1 and l2:
#         if alternator:
#             tail.next = l1
#             l1 = l1.next
#             alternator = False
#         else:
#             tail.next = l2
#             l2 = l2.next
#             alternator = True
#         tail = tail.next

#     if l1: tail.next = l1
#     else: tail.next = l2
#     return dummy.next

# def recursiveMerge(l1:node, l2:node):
#     if not l1 and not l2: return None
#     if not l1: return l2
#     if not l2: return l1

#     next1 = l1.next
#     next2 = l2.next
#     l1.next = l2
#     l2.next = recursiveMerge(next1, next2)
#     return l1

########### INSERT A NODE INTO A LINKED LIST AT A CERTAIN POSITION ##################

# def insertNode(head:node, position:int, data):
#     current = head  # our traverser
#     newNode = node(data) # in this case we had a piece of data we wanted to create into a new node
#     targetNext = None # variable to store the pointer of the item before the space we want to insert at. 
#                  # the pointer of this item would point to the item that would come after the inserted bit
#     index = 0
#     while current != None:
#         if index == position - 1: #see targetNext for why position - 1
#             targetNext = current.next
#             break
#         index += 1
#         current = current.next

#     if targetNext != None: #if the while loop it clause broke the loop
#         current.next = newNode #current.next pointer targets the newNode we want to insert
#         newNode.next = targetNext #newNode's pointer points to what current.next used to point to
#         return True

#     elif targetNext == None: #if targetNext == None, this means we never hit the if statement,
#         # and broke the loop with None. This means the index is out of range.
#         return IndexError('index out of range')

########### REMOVE A NODE AT A PARTICULAR INDEX WITH 2 TRAVERSERS ##################

def removeNode( head:node , index ):
    current = head
    nodeAfter:node = head.next
    position = 0
    temp = None
    while current != None:
        if position == index - 1:
            try:
                temp = nodeAfter
                nodeAfter = nodeAfter.next
                break
            except:
                raise IndexError('Index out of range!')
        
        current = current.next
        nodeAfter = nodeAfter.next
        position += 1
    
    if position == index - 1:
        current.next = nodeAfter
        del temp
        return True

    return False

print(reverseList(a))