
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])



def reverse(linked_list):
    
    new_list = LinkedList()
    node = linked_list.head
    
    while(node):
        new_list.append(node.value)
        node = node.next
        
    node = new_list.head
    temp = None
    temp2 = None
    while(node):
        temp2 = temp
        temp = node
        node = node.next
        temp.next = temp2
    new_list.head = temp
   
    
    return new_list


llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")





