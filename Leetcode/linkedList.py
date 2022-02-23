class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total +=1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)
    
    def get(self,index):
        if index>=self.length():
            print("Error: Index out of range!")
            return None
        cur_idx = 0 
        cur = self.head
        while True:
            cur = cur.next
            if cur_idx == index:
                return cur.data
            cur_idx +=1
    
    def erase(self, index):
        if index >= self.length():
            print("Error: Index out of range!")
            return
        cur_idx = 0 
        cur = self.head
        while True:
            lastNode = cur
            cur = cur.next
            if cur_idx == index:
                lastNode.next = cur.next
                return
            cur_idx += 1


my_list = linkedlist()
my_list.append(39)
my_list.append(40)
my_list.append(41)
my_list.append(42)
my_list.append(43)
my_list.append(44)
my_list.display()
my_list.erase(3)
my_list.display()